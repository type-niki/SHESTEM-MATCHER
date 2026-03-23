# SheSTEM AI: Study Group Matcher

> AI-powered study group formation for female STEM students  
> Advancing UN SDG 5 (Gender Equality) through technology

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 What It Does

Automatically creates optimal study groups for female STEM students based on:
- 📚 Shared courses
- 🤝 Complementary strengths/weaknesses  
- ⏰ Compatible schedules

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/type-niki/SHESTEM-MATCHER.git
cd SHESTEM-MATCHER

# Install dependencies
pip install -r requirements.txt

# Run the matcher
python student_matcher.py
```

## 📊 Output

The system generates:

**Console Output:**
```
Processing 12 female STEM students...

Study Group 1 (Compatibility Score: 555)
  - Alice Wanjiku: Strong in Math, needs Programming help
  - Betty Akinyi: Strong in Programming, needs Math help
  ...
```

**5 Visualization Charts:**
- `compatibility_scores.png` - Group matching quality
- `group_sizes.png` - Student distribution
- `course_coverage.png` - Course coverage heatmap
- `skills_distribution.png` - Skill diversity analysis
- `time_compatibility.png` - Schedule compatibility

## 🌍 Social Impact

**Problem:** Female STEM students drop out at 2.5× the rate of male students due to isolation.

**Solution:** Automatically form supportive peer study groups.

**UN SDG Alignment:** SDG 5 (Gender Equality) - Using AI to close the STEM gender gap.

## 🛠️ Tech Stack

- **Python 3.8+** - Core language
- **scikit-learn** - Machine learning library
- **matplotlib/seaborn** - Data visualization
- **pandas/numpy** - Data processing

## 📖 Documentation

See [`toolkit.md`](toolkit.md) for:
- Complete setup guide
- AI prompts used
- Learning reflections
- Common issues & fixes

## 🧪 How It Works

### Algorithm Overview
```
Student Data → Feature Engineering → Compatibility Scoring → 
Group Optimization → Visualization Pipeline
```

### Compatibility Formula
```
Score = (Shared courses × 20) + 
        (Complementary skills × 25) + 
        (Common free time × 15)
```

**Example Match:**
- Alice: Strong in Math, weak in Programming
- Betty: Strong in Programming, weak in Math
- **Result:** High compatibility! They help each other.

## 📁 Project Structure
```
shestem-matcher/
├── student_matcher.py      # Core matching algorithm
├── test_data.py           # Sample student data
├── visualizations.py      # Chart generation
├── requirements.txt       # Dependencies
├── toolkit.md            # Complete documentation
├── README.md             # This file
└── *.png                 # Generated visualizations
```

## 🎓 Use Cases

- **Universities:** Reduce female STEM dropout rates
- **Study Groups:** Optimize peer learning
- **Academic Support:** Proactive intervention
- **She Codes Africa:** Community building

## 🔮 Future Enhancements

- [ ] Database integration (MySQL)
- [ ] Web interface (Flask/React)
- [ ] WhatsApp group auto-creation
- [ ] Real-time group updates
- [ ] Impact measurement dashboard

## 👩‍💻 Author

**Renne Nekesa**  
GitHub: [@type-niki](https://github.com/type-niki)  
Project: Moringa AI Capstone 2026

## 📄 License

MIT License - Feel free to use and adapt!

## 🙏 Acknowledgments

- **Moringa School** - AI Capstone Project
- **She Codes Africa Chuka** - Community support
- **UN SDG 5** - Gender Equality inspiration

---

**Built with AI assistance in 6 hours** | **Addressing real social impact** | **Powered by scikit-learn**

