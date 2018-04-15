Easily move solution files from the FullStack-Lesson-Plans repo to your class repo in one simple bash/terminal command.

# Instructions
1. First, customize this line in `mover.py`:

    ```python
    instructorRepoPath = '/Users/jacobjanak/documents/code/trilogy/FullStack-Lesson-Plans'
    ```

    You should replace that string with your own path to the FullStack-Lesson-Plans repository.

2. Open terminal, bash, or command line and `cd` to the activity folder within the current week of your class repo. Basically, you should be inside an `01-Activities` folder. It is important that you are in the correct directory as this files behavior depends entirely on that! Then, run this command:

    `python <path-to-mover.py>`

3. Answer the questions it prompts you with.

![Alt text](./example.png?raw=true "Example")

4. A `Solved` folder should now appear inside the activity you specified!
