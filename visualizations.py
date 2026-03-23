"""
Visualization module for SheSTEM AI
Creates charts and graphs to visualize study group formations
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class GroupVisualizer:
    """Creates visualizations for study groups"""
    
    def __init__(self, groups, students):
        self.groups = groups
        self.students = students
    
    def plot_compatibility_scores(self, save_path='compatibility_scores.png'):
        """Bar chart of group compatibility scores"""
        plt.figure(figsize=(10, 6))
        
        group_names = [f"Group {i+1}" for i in range(len(self.groups))]
        scores = [g['score'] for g in self.groups]
        
        colors = sns.color_palette("viridis", len(scores))
        bars = plt.bar(group_names, scores, color=colors, edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        plt.xlabel('Study Groups', fontsize=12, fontweight='bold')
        plt.ylabel('Compatibility Score', fontsize=12, fontweight='bold')
        plt.title('Study Group Compatibility Scores\nHigher = Better Match', 
                 fontsize=14, fontweight='bold', pad=20)
        plt.ylim(0, max(scores) * 1.15)
        
        # Add average line
        avg_score = np.mean(scores)
        plt.axhline(y=avg_score, color='red', linestyle='--', linewidth=2, 
                   label=f'Average: {avg_score:.0f}')
        plt.legend(fontsize=10)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
        plt.close()
    
    def plot_group_sizes(self, save_path='group_sizes.png'):
        """Pie chart showing group size distribution"""
        plt.figure(figsize=(8, 8))
        
        sizes = [len(g['members']) for g in self.groups]
        labels = [f"Group {i+1}\n({size} students)" for i, size in enumerate(sizes)]
        
        colors = sns.color_palette("pastel", len(sizes))
        explode = [0.05] * len(sizes)  # Slightly separate slices
        
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
               colors=colors, explode=explode, shadow=True, textprops={'fontsize': 11})
        
        plt.title('Study Group Size Distribution', fontsize=14, fontweight='bold', pad=20)
        plt.axis('equal')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
        plt.close()
    
    def plot_course_coverage(self, save_path='course_coverage.png'):
        """Heatmap showing which courses each group covers"""
        # Get all unique courses
        all_courses = set()
        for student in self.students:
            all_courses.update(student.courses)
        all_courses = sorted(all_courses)
        
        # Create matrix: rows = groups, cols = courses
        matrix = []
        group_labels = []
        
        for i, group_info in enumerate(self.groups):
            group = group_info['members']
            group_labels.append(f"Group {i+1}")
            
            row = []
            for course in all_courses:
                # Count how many students in this group take this course
                count = sum(1 for s in group if course in s.courses)
                row.append(count)
            matrix.append(row)
        
        # Create heatmap
        plt.figure(figsize=(12, 6))
        sns.heatmap(matrix, annot=True, fmt='d', cmap='YlGnBu',
                   xticklabels=all_courses, yticklabels=group_labels,
                   cbar_kws={'label': 'Number of Students'}, linewidths=0.5)
        
        plt.xlabel('Courses', fontsize=12, fontweight='bold')
        plt.ylabel('Study Groups', fontsize=12, fontweight='bold')
        plt.title('Course Coverage per Study Group\n(Number of students taking each course)', 
                 fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
        plt.close()
    
    def plot_skills_distribution(self, save_path='skills_distribution.png'):
        """Bar chart showing skill distribution across groups"""
        # Collect all strengths
        all_strengths = []
        for student in self.students:
            all_strengths.extend(student.strengths)
        
        # Count frequency
        strength_counts = Counter(all_strengths)
        
        # Create plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Overall skill distribution
        skills = list(strength_counts.keys())
        counts = list(strength_counts.values())
        
        colors = sns.color_palette("rocket", len(skills))
        ax1.barh(skills, counts, color=colors, edgecolor='black', linewidth=1)
        ax1.set_xlabel('Number of Students', fontsize=11, fontweight='bold')
        ax1.set_title('Overall Skill Distribution\n(Student Strengths)', 
                     fontsize=12, fontweight='bold')
        ax1.invert_yaxis()
        
        # Add value labels
        for i, (skill, count) in enumerate(zip(skills, counts)):
            ax1.text(count + 0.1, i, str(count), va='center', fontsize=10, fontweight='bold')
        
        # Group skill coverage
        group_skills = []
        group_names = []
        for i, group_info in enumerate(self.groups):
            group = group_info['members']
            group_names.append(f"Group {i+1}")
            
            # Count unique skills in group
            unique_skills = set()
            for student in group:
                unique_skills.update(student.strengths)
            group_skills.append(len(unique_skills))
        
        colors2 = sns.color_palette("mako", len(group_names))
        bars = ax2.bar(group_names, group_skills, color=colors2, edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        ax2.set_ylabel('Unique Skills in Group', fontsize=11, fontweight='bold')
        ax2.set_title('Skill Diversity per Group\n(Unique strengths)', 
                     fontsize=12, fontweight='bold')
        ax2.set_ylim(0, max(group_skills) * 1.15)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
        plt.close()
    
    def plot_time_compatibility(self, save_path='time_compatibility.png'):
        """Chart showing common time slots per group"""
        plt.figure(figsize=(10, 6))
        
        group_names = [f"Group {i+1}" for i in range(len(self.groups))]
        common_time_counts = [len(g['common_time']) for g in self.groups]
        
        colors = sns.color_palette("coolwarm", len(self.groups))
        bars = plt.bar(group_names, common_time_counts, color=colors, 
                      edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        plt.xlabel('Study Groups', fontsize=12, fontweight='bold')
        plt.ylabel('Number of Common Time Slots', fontsize=12, fontweight='bold')
        plt.title('Schedule Compatibility per Group\n(More = Easier to meet)', 
                 fontsize=14, fontweight='bold', pad=20)
        plt.ylim(0, max(common_time_counts) * 1.2 if common_time_counts else 5)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Saved: {save_path}")
        plt.close()
    
    def create_all_visualizations(self):
        """Generate all visualization charts"""
        print("\nGenerating visualizations...")
        print("-" * 60)
        
        self.plot_compatibility_scores()
        self.plot_group_sizes()
        self.plot_course_coverage()
        self.plot_skills_distribution()
        self.plot_time_compatibility()
        
        print("-" * 60)
        print("All visualizations created successfully!")
        print("\nGenerated files:")
        print("  - compatibility_scores.png")
        print("  - group_sizes.png")
        print("  - course_coverage.png")
        print("  - skills_distribution.png")
        print("  - time_compatibility.png")