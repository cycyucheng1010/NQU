# 二元搜尋樹的加入、刪除與修改
# File Name: BinSearchTree.py
# Version

import sys

class Student:
    name = '' # 學生姓名
    score = 0 # 學生成績
    phone = ''
    llink = None # 左子鏈結
    rlink = None # 右子鏈結

root = None
i=0
datas = []
lists = [[]]
# 新增函數；新增一筆新的資料
def insert_f():
    name = ''
    score = 0
    print('\n=====INSERT DATA=====')
    name = input('Enter student name: ')
    score = eval(input('Enter student score: '))
    phone =input('Enter student phone: ')

    access(name, score, phone)

# 刪除函數；將資料從二元搜尋樹中刪除
def delete_f():
    global root
    name = ''
    if root == None:
        print('No student record!')
        return
    print('\n=====DELETE DATA=====')
    name = input('Enter student name: ')

    removing(name)

# 修改函數；修改學生成績
def modify_f():
    global root
    node = None
    name = ''
    if root == None: # 判斷根節點是否為空
        print('No student record!')
        return
    else:
        print('\n=====MODIFY DATA=====')
        name = input('Enter student name: ')

        node = search(name)
        if node == None:
            print('Student %s not found!' % name)
        else:
            #列出原資料狀況
            print('Original student name: ', node.name)
            print('Original student score: ', node.score)
            node.score = eval(input('Enter new score: '))
            print('Student %s has been modified' % name)

def modify_p():
    global root
    node = None
    name = ''
    if root == None: # 判斷根節點是否為空
        print('No student record!')
        return
    else:
        print('\n=====MODIFY DATA=====')
        name = input('Enter student name: ')

        node = search(name)
        if node == None:
            print('Student %s not found!' % name)
        else:
            #列出原資料狀況
            print('Original student name: ', node.name)
            print('Original student phone number: ', node.phone)
            node.phone = input('Enter new phone number: ')
            print('Student %s has been modified' % name)
# 輸出函數；依照人名由小至大輸出至螢幕
def show_f():
    global root
    global datas
    global lists
    global i
    if root == None: # 判斷根節點是否為空
        print('No student record!')
        return
    print('\n=====SHOW DATA=====')
    lists.clear()
    i=0
    inorder(root) # 以中序法輸出資料
    lists.sort(key=lambda x: x[1], reverse=True)
    for l in lists:
        print('%-10s %-10d %-10s' % (l[0], l[1], l[2]))
# 處理二元搜尋樹，將新增資料加入至二元搜尋樹中
def access(name, score, phone):
    global root
    node = None
    prev = None
    if search(name) != None: #資料已存在則顯示錯誤
        print('Student %s has existed!' % name)
        return
    ptr = Student()
    ptr.name = name
    ptr.score = score
    ptr.phone = phone
    ptr.llink = None
    ptr.rlink = None
    if root == None: # 當根節點為空的狀況
        root = ptr
    else: # 當根節點不為空的狀況
        node = root
        while node != None: # 搜尋資料插入點
            prev = node
            if ptr.name < node.name:
                node = node.llink
            else:
                node = node.rlink
        if ptr.name < prev.name:
            prev.llink = ptr
        else:
            prev.rlink = ptr

# 將資料從二元搜尋樹中移除
def removing(name):
    global root
    del_node = search(name)
    if del_node == None: # 找不到資料則顯示錯誤
        print('Student %s not found!' % name)
        return

    # 節點不為樹葉節點的狀況
    if del_node.llink != None or del_node.rlink != None:
        del_node = replace(del_node)
    else:
        if del_node == root:
            root = None
        else:
            connect(del_node, 'n')
    del_node = None # 釋放記憶體
    print('Student %s has been deleted!' % name)

# 尋找刪除非樹葉節點的替代節點
def replace(node):
    re_node = None
    # 當右子樹找不到替代節點，會搜尋左子樹是否存在替代節點
    re_node = search_re_r(node.rlink)
    if re_node == None:
        re_node = search_re_l(node.llink)
    if re_node.rlink != None: # 當替代節點有右子樹存在的狀況
        connect(re_node, 'r')
    elif re_node.llink != None: # 當替代節點有左子樹存在的狀況
        connect(re_node, 'l')
    else: # 當替代節點為樹葉節點的狀況
        connect(re_node, 'n')
    node.name = re_node.name
    node.score = re_node.score
    return re_node

# 調整二元搜尋樹的鏈結，link為r表示處理右鏈結、為l表示處理左鏈結、
# 為n則將鏈結指向None
def connect(node, link):
    parent = search_p(node) # 搜尋父節點
    if node.name < parent.name: # 節點為父節點左子樹的狀況
        if link == 'r': # link為r
            parent.llink = node.rlink
        elif link == 'l': # link為l
            parent.llink = node.llink
        else: # link為n
            parent.llink = None
    elif link == 'r': # 節點為父節點右子樹的狀況，link為r
        parent.rlink = node.rlink
    elif link == 'l': # link 為 l
        parent.rlink = node.llink
    else: # link為n
        parent.rlink = None

# 以中序法輸出資料，採遞迴方式
def inorder(node):
    datas = []
    global lists
    global i
    if (node != None):
        inorder(node.rlink)
        inorder(node.llink)
        datas.append(node.name)
        datas.append(node.score)
        datas.append(node.phone)
        lists.append(datas)
        i += 1


# 搜尋target所在節點
def search(target):
    global root
    node = root
    while node != None:
        if target == node.name:
            return node
        elif target < node.name: # target小於目前節點，往左搜尋
            node = node.llink
        else: # target大於目前節點，往右搜尋
            node = node.rlink

    return node

# 搜尋右子樹替代節點
def search_re_r(node):
    re_node = node
    while re_node != None and re_node.llink != None:
        re_node = re_node.llink
    return re_node

# 搜尋左子樹替代節點
def search_re_l(node):
    re_node = node
    while re_node != None and re_node.rlink != None:
        re_node = re_node.rlink
    return re_node

# 搜尋node的父節點
def search_p(node):
    global root
    parent = root
    while parent != None:
        if node.name < parent.name:
            if node.name == parent.llink.name:
                return parent
            else:
                parent = parent.llink
        elif node.name == parent.rlink.name:
            return parent
        else:
            parent = parent.rlink
    return None

def main():
    option = ''
    while True:
        print()
        print('**************************')
        print('       <1> insert         ')
        print('       <2> delete         ')
        print('       <3> modify score   ')
        print('       <4> modify phone   ')
        print('       <5> show           ')
        print('       <6> quit           ')
        print('**************************')

        try:
            option = input('Enter your choice: ')
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if option == '1':
            insert_f()
        elif option == '2':
            delete_f()
        elif option == '3':
            modify_f()
        elif option == '4':
            modify_p()            
        elif option == '5':
            show_f()
        elif option == '6':
            sys.exit(0)
        else:
            print('Wrong option!')

main()
