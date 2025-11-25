<img width="2220" height="933" alt="diagram-export-11-25-2025-9_48_09-AM" src="https://github.com/user-attachments/assets/a69a7a13-d7d4-4a2b-8e11-2fa2c3e60214" />

***1. PROBLEM STATEMENT:***
Learning French can feel overwhelming for beginners because it requires constant practice and quick feedback. I went through the same struggle when I started - remembering vocabulary, identifying noun genders in exams, and endless verb conjugations. Since teachers can’t be available all the time, and books don’t adapt to your pace, progress can feel slow.

Madame-Lexique fixes that by acting as a friendly AI French tutor. It helps you build vocabulary, learn grammar quickly, understand genders, conjugate verbs, and even gives personalized quizzes. The goal is to make French learning simple, interactive, and fun for everyone.

***2. WHY AGENTS?***
Agents are ideal for this problem because:
1. They can reason about the user’s intent and choose the correct tool automatically.
2. They provide consistent, instant feedback.
3. They allow knowledge (and familiar vocabulary) to be stored, updated, and reused.
4. They manage multiple tasks like meanings, verb conjugation, translation, and quizzes in a single system.
Instead of building separate applications for each capability, agents sync many tools and provide an easier and efficient learning process.

***OVERALL ARCHITECTURE***
The system has 3 main components: 

1. The Agent (Madame-Lexique): This is the brain. It understands user prompts, decides which tool to call, and explains French grammar and vocabulary.

2. The Tools:
- add_word (Saves new vocabulary entered or explained by the agent)
- get_meaning (Retrieves stored meanings from the vocab JSON file)
- generate_quiz (Produces quiz questions and checks user answers)
- conjugate_verb (Agent can produce a full conjugation)
- detect_gender (Determines the gender/article of nouns)
- translate_sentence (Translates full sentences)

3. The JSON Database:
A simple vocab.json file stores all words and their meanings. Whenever a new word is added, the file updates instantly.

***DEMO:***

