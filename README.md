# Just Do It
 

# Features overview of the product:
1. Add / edit / remove a todo task, with a title and a DDL.
2. After added, all task will be sorted by DDL in ascending order, finish the nearest DDL first!
3. Each task has three status: todo, in progress, and complete. You can click the button to simply change and see the status. After 'complete' status, another click will automatically delete the task. Either leave the task with pride, or delete it instantly, your choice!

# Instruction of usage:
1. Installation:
- If you have installed git, you can clone the project with typing the following code in terminal(Windows) or terminal(Mac) git clone https://github.com/tianhaotiger/Just-Do-It.git
- If you don't have git command, you can download the zip file and unzip in the folder where you wish to install it.
- ![1649661164(1)](https://user-images.githubusercontent.com/62366288/162684011-8d4c1c4b-10f9-4618-99f3-e3b35bb289f8.png)
- After you finish, open the project with an IDE(PyCharm, VSCode, etc), or you can use the terminal to open the folder.
- Create a Virtual environment.
- ![1649663688(1)](https://user-images.githubusercontent.com/62366288/162690603-6bbf1da0-76f3-438a-8866-6300066c3349.png)
- After creating the environment, activate it by running :
- ![1649663722(1)](https://user-images.githubusercontent.com/62366288/162690672-0f1bf00a-7759-40e7-bc06-4f68abc2a05f.png)
- Then remember to run 'pip install -r requirements.txt' in the parent folder. (If you encounter gbk codec error, refer to this blog:https://github.com/google/tangent/pull/9 .)

2. Quickstart:
- After installation, run 'flask run' in your terminal, then goto the 'http://127.0.0.1:5000/create-task' to see the page of todo list.
- ![1649661830(1)](https://user-images.githubusercontent.com/62366288/162685642-db6a8aef-ccfa-451e-8a2d-697457004ef1.png)
Add / edit / remove the task with the three icon showed in the picture.

![1649661883(1)](https://user-images.githubusercontent.com/62366288/162685788-fe7ca5c1-7d89-4e14-b1e6-bee48c0ceaea.png)

- Fill in the task title, and a DDL, then your task is created!

![1649661946(1)](https://user-images.githubusercontent.com/62366288/162685962-70860fef-bbac-472e-8807-07aec286fbcc.png)

- When you want to change a title or ddl of a certain task, click the edit button, and change the task. Remeber: you have to input the task ID as the arrow pointed to change the right task!

![1649662037(1)](https://user-images.githubusercontent.com/62366288/162686190-d5e370bf-2de9-46f0-94a2-ce7f74e19dfd.png)

- The DDL is sorted with ascending DDL order. And you can click the status button to change the task status from ToDo, In process, and Complete. After Complete, another click will delete the task!


3. Future Plan:
- Sort by status and ddl
- Let edit can be done with typing ID
- Have a button to filter all todo, in progress, complete task
- Have a button to stick a certain task to the top, show priority.
