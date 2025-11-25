<img width="2220" height="933" alt="Madame-Lexique-Flowchart" src="https://github.com/user-attachments/assets/01750f1a-ba76-4d77-acef-04ce1f835372" />


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
A simple vocab_data.json file stores all words and their meanings. Whenever a new word is added, the file updates instantly.

***DEMO:***
Basic Testing: 
<img width="1113" height="582" alt="Madame-Lexique-Convo" src="https://github.com/user-attachments/assets/95e4d53d-b282-4aa6-9b40-145d50e67f3e" />

Quiz Generation: 
<img width="827" height="360" alt="Madame-Lexique-Quiz" src="https://github.com/user-attachments/assets/ba666d9c-8ab6-434e-bf0f-5d0dba331fd2" />


***FUTURE IMPROVEMENTS:***

1. Add audio pronunciations
2. Build a web UI where students can chat with Madame-Lexique visually
3. Add difficulty levels for quizzes
4. Expand to French-to-French explanations for advanced learners
5. Make the agent store common mistakes to strengthen weak vocabulary areas
6. Add a progress tracker showing what the user has learned

