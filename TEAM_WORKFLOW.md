# 🧭 Team Workflow Guide for FakeNews_Spam_Detection

Hi all 👋  
The **main branch** is now protected — no one can push directly.  
Follow these steps to contribute safely and keep the repo clean.

---

## 🪜 Step 1: Clone the Repository

```bash
git clone https://github.com/ajayram231210006/FakeNews_Spam_Detection.git
cd FakeNews_Spam_Detection
🪜 Step 2: Create a New Branch for Your Task
(Use your name or task name in the branch for clarity.)

bash
Copy code
git checkout -b feature/aniket_feature_extraction
# or
git checkout -b feature/abhishek_model_training
💡 Naming convention:
Use lowercase letters and underscores for consistency, e.g.

feature/aniket_feature_extraction

fix/abhishek_bug_patch

docs/team_workflow

🪜 Step 3: Make Your Changes
Add your notebooks, scripts, or reports to the appropriate folders:

bash
Copy code
notebooks/, src/, reports/
⚠️ Do not modify or commit files in data/ — they’re ignored by .gitignore.
⚠️ Do not commit large datasets or model files.

🪜 Step 4: Stage and Commit Your Changes
bash
Copy code
git add .
git commit -m "Added feature extraction code"
✅ Tip: Keep commits small, clear, and meaningful.

🪜 Step 5: Push Your Branch to GitHub
bash
Copy code
git push origin feature/aniket_feature_extraction
🪜 Step 6: Open a Pull Request (PR)
Go to your repository on GitHub.

You’ll see a prompt saying “Compare & pull request.”

Click it → Add a title and short description → Click Create pull request.

Example:

Title: Add Feature Extraction Module

Description: Implemented TF-IDF vectorizer and preprocessing pipeline.

🪜 Step 7: Wait for Review/Approval
Ajayram (or another teammate) will review and approve the PR.
After approval, it will be merged into the main branch.

✅ Key Rules
🚫 Do not push directly to main.
🌿 Always create a new branch for every task.
👍 Get at least one approval before merging.
✍️ Keep commits small and meaningful.

Let’s keep the repo clean, organized, and conflict-free 💪

🧾 Quick Summary
Step Action Command
1 Clone repo git clone <repo-url>
2 Create new branch git checkout -b feature/<name>
3 Commit changes git add . && git commit -m "<msg>"
4 Push branch git push origin <branch>
5 Open PR via GitHub UI
6 Wait for review Get approval before merge

✨ Author
Ajayram Meena
Maintainer — FakeNews_Spam_Detection Team Workflow

