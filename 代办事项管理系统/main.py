# 极简待办事项系统（简历可用）
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 临时存储数据
todos = []

# 首页：展示待办
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# 添加任务
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append({"task": task, "done": False})
    return redirect('/')

# 标记完成
@app.route('/done/<int:id>')
def done(id):
    if 0 <= id < len(todos):
        todos[id]['done'] = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)