# Getting Started with scikit-learn for Student Matching

## 1. Overview

**Technology:** scikit-learn (Python ML Library)  
**Project:** AI-powered study group matcher for female STEM students  
**Goal:** Learn ML fundamentals by solving a real social problem (UN SDG 5)  
**Time to Complete:** 2-3 hours  

---

## 2. What is scikit-learn?

scikit-learn is Python's most popular machine learning library, used by:
- Netflix (recommendations)
- Banks (fraud detection)  
- LinkedIn (people matching)

**Our Use Case:** Match students into study groups based on compatibility.

---

## 3. Quick Start

### Requirements
- Python 3.8+
- 20 minutes setup time

### Installation
```bash
# Create project
mkdir shestem-matcher && cd shestem-matcher

# Install dependencies
pip install scikit-learn pandas numpy matplotlib seaborn

# Verify
python -c "import sklearn; print('Ready!')"
```

---

## 4. How It Works

### The Algorithm

**Input:** 12 students with:
- Courses they're taking
- Their strengths/weaknesses
- Free time slots

**Process:**
1. Calculate compatibility between each pair of students
2. Find optimal groups of 3-4 using combinations
3. Generate visualizations

**Output:**
- 3 study groups
- Compatibility scores
- 5 visualization charts

### Compatibility Scoring
```
Score = (Shared courses × 20) + 
        (Complementary skills × 25) + 
        (Common free time × 15)
```

**Example:**
- Alice: Strong in Math, weak in Programming
- Betty: Strong in Programming, weak in Math
- **Compatibility: High!** (They help each other)

---

## 5. Running the Code
```bash
python student_matcher.py
```

**Output:**
```
Study Group 1 (Score: 555)
  - Alice: Math expert, needs Programming help
  - Betty: Programming expert, needs Math help
  - Carol: Balanced skills
  
  Why this works: Alice helps Betty with Math,
                   Betty helps Alice with Programming
```

**Plus 5 charts:** compatibility_scores.png, group_sizes.png, etc.

---

## 6. AI Prompts I Used

| What I Needed | Prompt | Result |
|---------------|--------|--------|
| Understand ML basics | "Explain scikit-learn for matching students" | Learned about feature vectors |
| Convert data to numbers | "How to encode student courses for ML?" | Binary encoding strategy |
| Find best groups | "Python algorithm for optimal grouping" | Use itertools.combinations |
| Make charts | "Visualize group results with matplotlib" | 5 different chart types |

**AI saved me ~15 hours** of reading documentation!

---

## 7. Common Problems

**Problem:** Can't import sklearn  
**Fix:** `pip install scikit-learn` (install name ≠ import name)

**Problem:** Slow with many students  
**Fix:** Algorithm checks all combinations - use greedy approach for 20+ students

**Problem:** No charts generated  
**Fix:** Check current directory: `ls *.png`

---

## 8. What I Learned

**Technical Skills:**
- Feature engineering (converting real data to ML format)
- Algorithm optimization (balancing speed vs quality)
- Data visualization (matplotlib/seaborn)

**ML Concepts:**
- Similarity scoring
- Combinatorial optimization
- Trade-offs between exhaustive vs greedy search

**Using AI:**
- AI is great for learning syntax and concepts
- Still need to understand and adapt suggestions
- Testing is crucial - AI can't do that for you

**Time Impact:** What would take 2 weeks took 2 days with AI help!

---

## 9. Next Steps

**To improve this project:**
1. Add database (MySQL) for real student data
2. Build web interface (Flask)
3. Connect to WhatsApp API for auto-groups
4. Measure actual impact on student retention

**To learn more ML:**
- Try classification problems (spam detection)
- Try regression (price prediction)
- Explore deep learning (TensorFlow)

---

## 10. Social Impact

**Problem Solved:** Female STEM students drop out at 2.5× the rate of males due to isolation.

**Our Solution:** Automatic peer support groups reduce isolation.

**UN SDG Alignment:** SDG 5 (Gender Equality) - using tech to close the STEM gender gap.

**Measurable Impact:** Target 30% reduction in dropout rates.

---

## Resources

- [scikit-learn Documentation](https://scikit-learn.org/)
- [Code Repository](your-github-link)
- [Full Code Files](see GitHub)

---

**Project Stats:**
- Time: 6 hours total (4 coding + 2 debugging)
- Lines of Code: ~400
- AI Prompts Used: 5 key prompts
- Learning Outcome: Went from "What is ML?" to working AI system

**Difficulty:** Intermediate  
**Suitable For:** Python developers learning ML  
**Production Ready:** POC (needs scaling work)