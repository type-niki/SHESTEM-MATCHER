"""
SheSTEM AI: Student Matching System
Automatically forms study groups for female STEM students
"""

class Student:
    """Represents a female STEM student"""
    
    def __init__(self, student_id, name, courses, strengths, weaknesses, free_time=None):
        self.student_id = student_id
        self.name = name
        self.courses = set(courses)
        self.strengths = set(strengths)
        self.weaknesses = set(weaknesses)
        self.free_time = set(free_time) if free_time else set()
    
    def __repr__(self):
        return f"Student({self.name})"


class StudyGroupMatcher:
    """Matches students into optimal study groups"""
    
    def __init__(self, min_group_size=3, max_group_size=5):
        self.min_group_size = min_group_size
        self.max_group_size = max_group_size
    
    def calculate_compatibility(self, student1, student2):
        """Calculate compatibility score between two students"""
        score = 0
        
        # Shared courses
        common_courses = student1.courses & student2.courses
        score += len(common_courses) * 20
        
        # Complementary strengths
        if student1.weaknesses & student2.strengths:
            score += 25
        if student2.weaknesses & student1.strengths:
            score += 25
        
        # Compatible schedule
        common_time = student1.free_time & student2.free_time
        score += len(common_time) * 15
        
        return score
    
    def calculate_group_score(self, group):
        """Calculate total compatibility score for a group"""
        total_score = 0
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                total_score += self.calculate_compatibility(group[i], group[j])
        return total_score
    
    def find_best_group(self, students, group_size):
        """Find the best group of specified size"""
        from itertools import combinations
        
        best_group = None
        best_score = -1
        
        for combo in combinations(students, group_size):
            score = self.calculate_group_score(list(combo))
            if score > best_score:
                best_score = score
                best_group = list(combo)
        
        return best_group, best_score
    
    def form_study_groups(self, students):
        """Form optimal study groups from list of students"""
        groups = []
        remaining = students.copy()
        
        while len(remaining) >= self.min_group_size:
            if len(remaining) >= self.max_group_size:
                group_size = self.max_group_size
            else:
                group_size = len(remaining)
            
            best_group, score = self.find_best_group(remaining, group_size)
            
            if best_group:
                groups.append({
                    'members': best_group,
                    'score': score,
                    'common_courses': self._get_common_courses(best_group),
                    'common_time': self._get_common_time(best_group)
                })
                
                for student in best_group:
                    remaining.remove(student)
        
        if remaining:
            groups.append({
                'members': remaining,
                'score': self.calculate_group_score(remaining) if len(remaining) > 1 else 0,
                'common_courses': self._get_common_courses(remaining),
                'common_time': self._get_common_time(remaining),
                'note': 'Smaller group due to remaining students'
            })
        
        return groups
    
    def _get_common_courses(self, group):
        """Get courses shared by all members"""
        if not group:
            return set()
        common = group[0].courses
        for student in group[1:]:
            common = common & student.courses
        return common
    
    def _get_common_time(self, group):
        """Get time slots available to all members"""
        if not group:
            return set()
        common = group[0].free_time
        for student in group[1:]:
            common = common & student.free_time
        return common
    
    def _find_complementary_pairs(self, group):
        """Find complementary student pairs in group"""
        pairs = []
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                s1, s2 = group[i], group[j]
                if s1.weaknesses & s2.strengths:
                    skill = ', '.join(s1.weaknesses & s2.strengths)
                    pairs.append(f"{s2.name} can help {s1.name} with {skill}")
                if s2.weaknesses & s1.strengths:
                    skill = ', '.join(s2.weaknesses & s1.strengths)
                    pairs.append(f"{s1.name} can help {s2.name} with {skill}")
        return pairs if pairs else ["Members have complementary skills"]
    
    def display_groups(self, groups):
        """Pretty print study groups"""
        print("\n" + "=" * 60)
        print("SHESTEM AI - STUDY GROUP RECOMMENDATIONS")
        print("=" * 60)
        
        for i, group_info in enumerate(groups, 1):
            group = group_info['members']
            score = group_info['score']
            common_courses = group_info['common_courses']
            common_time = group_info['common_time']
            
            print(f"\nStudy Group {i} (Compatibility Score: {score})")
            print("-" * 60)
            
            for student in group:
                print(f"   - {student.name} ({student.student_id})")
                print(f"     Courses: {', '.join(student.courses)}")
                print(f"     Strong in: {', '.join(student.strengths) if student.strengths else 'N/A'}")
                print(f"     Needs help: {', '.join(student.weaknesses) if student.weaknesses else 'N/A'}")
            
            print(f"\n   > Shared courses: {', '.join(common_courses) if common_courses else 'None'}")
            print(f"   > Common time: {', '.join(common_time) if common_time else 'None'}")
            
            if len(group) > 1:
                print(f"   > Why this works:")
                complementary = self._find_complementary_pairs(group)
                for pair in complementary:
                    print(f"      * {pair}")
            
            if 'note' in group_info:
                print(f"   NOTE: {group_info['note']}")
        
        print("\n" + "=" * 60)


def main():
    """Main execution"""
    from test_data import create_sample_students
    from visualizations import GroupVisualizer
    
    students = create_sample_students()
    print(f"\nProcessing {len(students)} female STEM students...")
    
    matcher = StudyGroupMatcher(min_group_size=3, max_group_size=4)
    groups = matcher.form_study_groups(students)
    matcher.display_groups(groups)
    
    print(f"\nSummary:")
    print(f"   Total students: {len(students)}")
    print(f"   Groups formed: {len(groups)}")
    avg = sum(len(g['members']) for g in groups) / len(groups)
    print(f"   Average group size: {avg:.1f}")
    
    # Create visualizations
    print("\n" + "=" * 60)
    visualizer = GroupVisualizer(groups, students)
    visualizer.create_all_visualizations()
    print("=" * 60)


if __name__ == "__main__":
    main()