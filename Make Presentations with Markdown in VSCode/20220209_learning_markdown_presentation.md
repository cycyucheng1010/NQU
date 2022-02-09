---
marp: true
author: Rick Chen
size: 4:3
theme: gaia
---
<style>
    :root{
        --color-background: #101010;
        --color-foreground: #FFFFFF;
    }
</style>
# Using MARP to make PPT
* 在vscode 安裝marp 然後create new markdown file
* 在最上頭設定以下參數
```
---
marp: True # 開啟marp
author: Rick Chen #who
size: 4:3 # 可以調整成任何size
theme: gaia #可以選擇主題
---
```
---

# new pages
* 書寫跟markdown語法相同 可參考以下範例
    * **aaa**
    * _bbb_
    * `ccc`

---
* 上頁code如下:
```
# new pages
* 書寫跟markdown語法相同 可參考以下範例
    * **aaa**
    * _bbb_
    * `ccc`
```
* 利用```---```進行分隔，新增新的一頁
---
![test_img](img1.jpg)

---
## 你也可以透過設定html的style方式去做一些設定例如:
* 設定背景顏色以及字體顏色
```
<style>
    :root{
        --color-background: #101010;
        --color-foreground: #FFFFFF;
    }
</style>
```
---

# 存檔
* click the button 
![button](button.PNG)
* 選要哪個(PDF, PPTX,HTML,PNG,JPG)

---

# 參考資料
* [MARP - Make Presentations with Markdown in VSCode | Can it replace PowerPoint? | Better Data Science](https://www.youtube.com/watch?v=OmKtuBXNjac)

--- 

# **_Thank you for your watching_**