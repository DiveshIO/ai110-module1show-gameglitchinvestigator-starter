# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start.

(for example: "the secret number kept changing" or "the hints were backwards").

The secret number was high, but the program kept saying to go lower.

- They told us for different game modes we would be provided more attempts, but it was false.

- I notice when looking at the code, the range for normal was 0-100, while hard was 0-50, which makes no sense.

- Noticed the guess range estimate text was wrong

- The score was going below negative.

- When it's given over, the new game doesn't start.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example, ChatGPT, Gemini, Copilot)?

Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I had first run the code, then detected some bugs, and then I talked with Claude about if these were bugs and which codes caused these bugs.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI detected a bug about the score, but it said something wrong where it said to start from 0, but the score was 100, which was a bit confusing. When reasking with some tests, it fixed the starting score.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I tested the program and then asked Claude to write tests for the issue I had faced.

- Describe at least one test you ran (manual or using pytest).

and what it showed you about your code.

I ran the score test that Claude created, where it showed the actual score was 75, but the program got 105. Then we fixed the code.

- Did AI help you design or understand any tests? How?

It had helped me design the test but not understand where it just looked at the things I placed them in, commented, fixed them, and then wrote the test for them.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The secret number was not stored in a variable, so it kept changing where we had to store the variable.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain Streamlit rerun as. a script that will keep running the stream. and session state score the initial values.

- What change did you make that finally gave the game a stable secret number?

I had stored the secret number and not made it random, which helped.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

- This could be a testing habit, a prompting strategy, or a way you used Git.

- What is one thing you would do differently next time you work with AI on a coding task?

- In one or two sentences, describe how this project changed the way you think about AI-generated code.

Comparison between AI

Claude found 9 bugs, but they had mini bugs, which had to be detected by manual intervention.

ChatGPT found 11 bugs; it had found extra information, such as bits unique about log errors.

Gemini found 8 bugs, which were most critical for the game logic. That's all.
