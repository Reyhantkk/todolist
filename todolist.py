import json
from datetime import datetime, timedelta

class ToDoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def show_tasks(self):
        if not self.tasks:
            print("Görev yok.")
        else:
            print("Görevler:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['title']} - Bitiş Zamanı: {task['due_time']} - Tamamlandı: {task['completed']}")

    def add_task(self, title, due_time):
        new_task = {
            "title": title,
            "due_time": due_time,
            "completed": False
        }
        self.tasks.append(new_task)
        print(f"{title} görevi eklendi.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"{deleted_task['title']} görevi silindi.")
        else:
            print("Geçersiz görev numarası.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"{self.tasks[task_index - 1]['title']} görevi tamamlandı.")
        else:
            print("Geçersiz görev numarası.")

    def run(self):
        self.load_tasks()

        while True:
            print("\n1. Görevleri Göster")
            print("2. Görev Ekle")
            print("3. Görev Sil")
            print("4. Görev Tamamla")
            print("5. Çıkış")

            choice = input("Bir seçenek girin (1-5): ")

            if choice == "1":
                self.show_tasks()
            elif choice == "2":
                title = input("Görev adı girin: ")
                due_time_str = input("Bitiş zamanını (YYYY-MM-DD HH:MM) girin: ")
                due_time = datetime.strptime(due_time_str, "%Y-%m-%d %H:%M")
                self.add_task(title, due_time.strftime("%Y-%m-%d %H:%M"))
            elif choice == "3":
                task_index = int(input("Silmek istediğiniz görevin numarasını girin: "))
                self.delete_task(task_index)
            elif choice == "4":
                task_index = int(input("Tamamlanan görevin numarasını girin: "))
                self.complete_task(task_index)
            elif choice == "5":
                self.save_tasks()
                print("Çıkılıyor...")
                break
            else:
                print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
