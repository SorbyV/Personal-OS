Day 0 - 22/07
Started the project - my aim is to learn the latest in full stack development 1st, then later get hands-om with integrating an AI agent into the app. By the end of it, I want to polish my full stack development skills as well as learn AI fundamentals beyong using LLMs for coding. I will be working on this project emulating an engineering team, hence moving step by step, defining documents along the way.
Chalked out a basic vision document for the project, defining things like what this app does, who is it for, why am I building it, score of version 1, what does success look like for version 1.

Day 1 - 23/07
Started working towards the system architecture.
Started by defining a list of Modules to be included in Version1
Learning: A module is easily confused with a view, on basis that separation is visible in the UI. Instead, it might be better to think in terms of ownership. Is a journal affected if you remove say, a to-do reminder system from the app. Not really, so this might be a good separation point. 
Just because different parts of the app work in similar ways doesn't mean they are a single module. They might use the same utilities, but the ownership of responsibilities is still different. 
Ofcourse, in the end, its up to us to define the app architecture however we want.
##"Good architecture isn't about predicting the future. It's about making today's design easy to extend tomorrow."

Design Decisions

Version 1 will be decomposed into business domains rather than UI pages.
Homepage will aggregate information rather than own it.
AI architecture is intentionally deferred until the non-AI architecture is stable.