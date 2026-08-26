## GIT & GITHUB PRACTICAL ASSIGNMENT

### Assignment 2 — **Build, Branch & Submit**

**Type:** Individual
**Deadline:** Before our next session

### Scenario

Imagine that you have been asked to develop a small Python project that will eventually become part of a larger software system.

Your task is to create the project, manage it with Git, publish it on GitHub, and demonstrate the workflow we discussed during our Git & GitHub session.

### Task

Create a Python project called:

```text
student-information-system
```

Your program should collect the following information from a user:

* Full Name
* Student ID
* Programme
* Level
* Age
* Favourite Programming Language

Then, using **string concatenation** (not just printing the raw inputs), your program must **generate two new pieces of information** from what the user typed:

1. **A Student Username** — built by combining part of their name with their Student ID (e.g. first 3 letters of their name + Student ID).
2. **A Student Email** — built by combining their generated username with a fixed domain, e.g. `username + "@st.ug.edu.gh"`.

Finally, your program should build its own border/divider line using concatenation (e.g. joining `"="` characters together into one string variable) rather than typing out `========` directly wherever it's needed.

Your program should then display everything in a well-formatted manner. For example:

```text
========================================
       STUDENT INFORMATION SYSTEM
========================================

Full Name                  : Taylor Norbert
Student ID                 : 22447815
Programme                  : Information Technology
Level                      : 100
Age                        : 19
Favourite Language         : Python
Generated Username         : tay22447815
Generated Email            : tay22447815@st.ug.edu.gh

========================================
```

You may improve the design of the output.

---

## PART A — Git Repository Setup

Create a GitHub repository named:

```text
student-information-system
```

Create the project locally and initialise Git.

Your repository must contain at least:

```text
student-information-system/
│
├── student_information.py
├── README.md
└── .gitignore
```

Your `.gitignore` should exclude at least generated/system files (e.g. `__pycache__/`).

Your `README.md` should contain:

* Project title
* Short description of the project
* Features of the program (including how the username/email are generated)
* Your name
* Your GitHub username

---

## PART B — Commit History

Your project must have **at least 4 meaningful commits**, representing real stages of development.

For example:

```text
Initial project setup
Add input collection
Add generated username and email using string concatenation
Add formatted output with generated border
```

Do **not** make four meaningless commits simply to satisfy the requirement.

---

## PART C — Branching

You are **not allowed to make all your changes directly on `main`**.

Create a separate branch called:

```text
feature/student-registration
```

Make at least one meaningful improvement to the project from this branch — for example, improving how the username/email is generated, adding another concatenated field, or improving the README.

Commit your changes and push the branch to GitHub.

---

## PART D — Pull Request

Create a Pull Request from:

```text
feature/student-registration
```

into:

```text
main
```

Your Pull Request must have:

**A clear title**, e.g. `Add student registration information`

**A proper description** briefly explaining:

1. What you changed
2. Why you made the changes
3. What someone reviewing the Pull Request should look out for

---

## PART E — Collaboration

Add **GKA** as a collaborator on your repository.

GitHub username:

```text
GyasiAmosKwadwo
```

I should be able to access your repository and review your work.

---

## PART F — Final Submission

Submit the **GitHub repository URL** in the WhatsApp group.

Before submitting, make sure I can see:

* Your Python program
* Your README and `.gitignore`
* Your commit history
* Your feature branch
* Your Pull Request
* Your merged changes
* Your collaboration settings

---

# 🤝 ASSIGNMENT 2 — THE COLLABORATION CHALLENGE

**Type:** Pair Work
**Deadline:** Before our next session

This assignment is designed to simulate how developers actually work together on a software project.

You will work in pairs.

Each pair will have:

**Developer A — Repository Owner**

**Developer B — Contributor**

---

## THE PROJECT

Together, build a simple:

# 🎓 UNIVERSITY STUDENT PORTAL

The program should collect basic information about a student and display a student profile.

At minimum, collect:

* Full Name
* Student ID
* Programme
* Level
* Age
* Hall of Residence

Using **string concatenation**, the program must also generate:

* A **Student Email** built from parts of the name and Student ID (Developer A's feature — see below)
* A single **Contact Line** built by concatenating the generated email + Hall of Residence + Programme into one readable string, e.g. `"Reach " + name + " (" + programme + ") at " + email + ", " + hall` (Developer B's feature — see below)

Your final program should produce a clean output similar to:

```text
==================================================
             UNIVERSITY STUDENT PORTAL
==================================================

Student Profile

Full Name          : __________________
Student ID         : __________________
Programme          : __________________
Level              : __________________
Age                : __________________
Hall               : __________________
Generated Email    : __________________
Contact Line       : __________________

==================================================
          UNIVERSITY OF GHANA
==================================================
```

You are encouraged to make your interface better than the example.

---

## DEVELOPER A — REPOSITORY OWNER

You are responsible for:

1. Creating the GitHub repository (include a `.gitignore`).
2. Adding your partner as a collaborator.
3. Creating the initial project and `main` branch.
4. Making the initial commit.
5. Creating a branch for your own feature.
6. Implementing the **Student Registration + Generated Email** feature (built via string concatenation).
7. Pushing your branch to GitHub.
8. Reviewing your partner's Pull Request.

---

## DEVELOPER B — CONTRIBUTOR

You are responsible for:

1. Accepting the GitHub collaboration invitation.
2. Cloning the repository to your computer.
3. Creating your own feature branch.
4. Implementing the **Contact Line** feature — concatenating the email (from Developer A's work), hall, and programme into one combined string.
5. Committing your changes.
6. Pushing your branch to GitHub.
7. Creating a Pull Request into `main`.
8. Writing a proper Pull Request description.

---

# 🔍 PULL REQUEST REVIEW

Once Developer B creates the Pull Request, Developer A must review it before merging.

Go to **Pull Request → Files changed** and inspect the changes.

Developer A must leave **at least one meaningful review comment**.

For example:

> "The contact line concatenation works correctly, but consider adding a space after the comma for readability."

After the review, Developer A may approve and merge the Pull Request.

**Note:** Since Developer B's feature depends on Developer A's generated email, you may encounter a small merge conflict or dependency issue. This is intentional and part of the learning experience. Don't panic if it happens.

---

# 🌿 BRANCH REQUIREMENT

Your final repository should demonstrate at least:

```text
main
│
├── developer-a-feature
│
└── developer-b-feature
```

You do not have to use these exact branch names.

---

# 📋 WHAT WILL BE ASSESSED?

**1. Git Usage** — repository management, commits, branches, pushes

**2. GitHub Usage** — repository setup, collaboration, Pull Requests, reviews, merging

**3. Code** — Does the program work? Is the concatenation logic correct and readable? Are variable names understandable?

**4. Collaboration** — Did both developers contribute? Did each work on a separate, connected feature? Was the Pull Request properly reviewed?

**5. Documentation** — Is the README useful? Are commit messages meaningful? Is the Pull Request description clear?

---

## ⚠️ IMPORTANT

This assignment is **not about producing the most complicated Python program**.

I am interested in seeing whether you can take what we have learnt — variables, input, output, and string concatenation — and use it to manage a project properly.

If you encounter an error, **don't panic and don't immediately delete the project and start again.** Take a screenshot, investigate the error, and ask questions.

Remember:

> **Git is not something you master by memorising commands. You master it by using it.**

And finally, **do not copy another person's repository**. I want to see your own Git history, your own branches, your own commits, and your own contribution.

Good luck, developers. 🐍💻🔥