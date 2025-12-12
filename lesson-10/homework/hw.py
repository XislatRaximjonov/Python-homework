# =========================
#      TASK CLASS
# =========================
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"   # default status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"
    

# =========================
#     TODO LIST CLASS
# =========================
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"\nTask {i}:")
            print(task)

    def list_incomplete_tasks(self):
        incomplete = [t for t in self.tasks if t.status == "Incomplete"]
        if not incomplete:
            print("All tasks are complete!")
            return

        for i, task in enumerate(incomplete, 1):
            print(f"\nIncomplete Task {i}:")
            print(task)

    def mark_task_complete(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number!")
        else:
            self.tasks[index - 1].mark_complete()
            print("Task marked as complete!")


# =========================
#      MAIN PROGRAM
# =========================
def main():
    todo = ToDoList()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo.add_task(task)

        elif choice == "2":
            todo.list_all_tasks()
            num = int(input("Enter task number to mark complete: "))
            todo.mark_task_complete(num)

        elif choice == "3":
            todo.list_all_tasks()

        elif choice == "4":
            todo.list_incomplete_tasks()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again!")


# =========================
#       RUN PROGRAM
# =========================
if __name__ == "__main__":
    main()


# ======================================
#             POST CLASS
# ======================================
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Author: {self.author}\n"
        )


# ======================================
#             BLOG CLASS
# ======================================
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully!")

    def list_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for i, post in enumerate(self.posts, start=1):
            print(f"\nPost {i}:")
            print(post)

    def posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() == author.lower()]
        if not filtered:
            print("No posts found for this author.")
            return

        for i, post in enumerate(filtered, start=1):
            print(f"\nPost by {author} #{i}:")
            print(post)

    def delete_post(self, index):
        if index < 1 or index > len(self.posts):
            print("Invalid post number!")
        else:
            del self.posts[index - 1]
            print("Post deleted successfully!")

    def edit_post(self, index, new_title, new_content):
        if index < 1 or index > len(self.posts):
            print("Invalid post number!")
        else:
            self.posts[index - 1].title = new_title
            self.posts[index - 1].content = new_content
            print("Post updated successfully!")

    def latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
            return

        print(f"\nShowing latest {count} posts:")
        for post in self.posts[-count:]:
            print("\n" + str(post))


# ======================================
#           MAIN PROGRAM (CLI)
# ======================================
def main():
    blog = Blog()

    while True:
        print("\n========= BLOG MENU =========")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts By Author")
        print("4. Edit a Post")
        print("5. Delete a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.posts_by_author(author)

        elif choice == "4":
            blog.list_posts()
            index = int(input("Enter post number to edit: "))
            new_title = input("New title: ")
            new_content = input("New content: ")
            blog.edit_post(index, new_title, new_content)

        elif choice == "5":
            blog.list_posts()
            index = int(input("Enter post number to delete: "))
            blog.delete_post(index)

        elif choice == "6":
            count = int(input("How many latest posts? (e.g., 3): "))
            blog.latest_posts(count)

        elif choice == "7":
            print("Exiting blog system...")
            break

        else:
            print("Invalid choice, try again.")


# ======================================
#       RUN PROGRAM
# ======================================
if __name__ == "__main__":
    main()

# =======================================
#            ACCOUNT CLASS
# =======================================
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful!")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance! Overdraft not allowed.")

    def __str__(self):
        return (
            f"Account Number: {self.acc_number}\n"
            f"Holder Name: {self.holder_name}\n"
            f"Balance: {self.balance}"
        )


# =======================================
#              BANK CLASS
# =======================================
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Account created successfully!")

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(f"Balance for {acc.holder_name}: {acc.balance}")
        else:
            print("Account not found!")

    def deposit(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found!")

    def withdraw(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found!")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)

        if not sender:
            print("Sender account not found!")
            return

        if not receiver:
            print("Receiver account not found!")
            return

        if sender.balance < amount:
            print("Transfer failed! Not enough balance.")
            return

        sender.balance -= amount
        receiver.balance += amount
        print("Transfer successful!")

    def show_account_details(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print("\n=== Account Details ===")
            print(acc)
        else:
            print("Account not found!")


# =======================================
#            MAIN PROGRAM (CLI)
# =======================================
def main():
    bank = Bank()

    while True:
        print("\n========== BANK MENU ==========")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Show Account Details")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            balance = float(input("Initial balance: "))
            acc = Account(acc_num, name, balance)
            bank.add_account(acc)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_num, amount)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_num, amount)

        elif choice == "5":
            from_acc = input("Sender account number: ")
            to_acc = input("Receiver account number: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            acc_num = input("Enter account number: ")
            bank.show_account_details(acc_num)

        elif choice == "7":
            print("Exiting Banking System...")
            break

        else:
            print("Invalid choice! Try again.")


# =======================================
#                RUN
# =======================================
if __name__ == "__main__":
    main()
