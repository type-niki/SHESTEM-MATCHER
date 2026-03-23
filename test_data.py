"""
Sample data: 12 female STEM students for testing
"""

from student_matcher import Student


def create_sample_students():
    """Create sample female STEM students"""
    
    students = [
        Student(
            student_id="SCT211-001/2024",
            name="Alice Wanjiku",
            courses=["Programming", "Mathematics", "Physics"],
            strengths=["Mathematics"],
            weaknesses=["Programming"],
            free_time=["Monday 2-4pm", "Wednesday 3-5pm"]
        ),
        Student(
            student_id="SCT211-002/2024",
            name="Betty Akinyi",
            courses=["Programming", "Mathematics"],
            strengths=["Programming"],
            weaknesses=["Mathematics"],
            free_time=["Monday 2-4pm", "Thursday 1-3pm"]
        ),
        Student(
            student_id="SCT211-003/2024",
            name="Carol Njeri",
            courses=["Programming", "Physics", "Electronics"],
            strengths=["Physics"],
            weaknesses=["Programming"],
            free_time=["Wednesday 3-5pm", "Friday 2-4pm"]
        ),
        Student(
            student_id="SCT211-004/2024",
            name="Diana Muthoni",
            courses=["Mathematics", "Physics"],
            strengths=["Mathematics", "Physics"],
            weaknesses=["Chemistry"],
            free_time=["Monday 2-4pm", "Wednesday 3-5pm"]
        ),
        Student(
            student_id="SCT211-005/2024",
            name="Emma Chebet",
            courses=["Programming", "Mathematics", "Physics"],
            strengths=["Programming"],
            weaknesses=["Mathematics"],
            free_time=["Tuesday 1-3pm", "Thursday 1-3pm"]
        ),
        Student(
            student_id="SCT211-006/2024",
            name="Fatima Hassan",
            courses=["Mathematics", "Physics", "Chemistry"],
            strengths=["Physics", "Chemistry"],
            weaknesses=["Mathematics"],
            free_time=["Wednesday 3-5pm", "Friday 2-4pm"]
        ),
        Student(
            student_id="SCT211-007/2024",
            name="Grace Wambui",
            courses=["Programming", "Mathematics"],
            strengths=["Mathematics"],
            weaknesses=["Programming"],
            free_time=["Monday 2-4pm", "Thursday 1-3pm"]
        ),
        Student(
            student_id="SCT211-008/2024",
            name="Hannah Adhiambo",
            courses=["Programming", "Physics", "Electronics"],
            strengths=["Programming", "Electronics"],
            weaknesses=["Physics"],
            free_time=["Tuesday 1-3pm", "Friday 2-4pm"]
        ),
        Student(
            student_id="SCT211-009/2024",
            name="Ivy Nyambura",
            courses=["Mathematics", "Physics"],
            strengths=["Mathematics", "Physics"],
            weaknesses=["Programming"],
            free_time=["Monday 2-4pm", "Wednesday 3-5pm"]
        ),
        Student(
            student_id="SCT211-010/2024",
            name="Jane Wanjiru",
            courses=["Programming", "Mathematics", "Electronics"],
            strengths=["Programming"],
            weaknesses=["Electronics"],
            free_time=["Thursday 1-3pm", "Friday 2-4pm"]
        ),
        Student(
            student_id="SCT211-011/2024",
            name="Khadija Omar",
            courses=["Physics", "Chemistry", "Mathematics"],
            strengths=["Chemistry"],
            weaknesses=["Physics"],
            free_time=["Wednesday 3-5pm", "Friday 2-4pm"]
        ),
        Student(
            student_id="SCT211-012/2024",
            name="Lucy Nduta",
            courses=["Programming", "Mathematics"],
            strengths=["Programming", "Mathematics"],
            weaknesses=[],
            free_time=["Monday 2-4pm", "Tuesday 1-3pm"]
        ),
    ]
    
    return students


if __name__ == "__main__":
    students = create_sample_students()
    print(f"Created {len(students)} sample students")
    for s in students:
        print(f"  - {s.name}: {', '.join(s.courses)}")