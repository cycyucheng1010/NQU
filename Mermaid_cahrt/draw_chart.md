# 在github上畫圖表
## 前言
* 前陣子github開放了mermaid在github上的markdown使用
* mermaid是一個markdown的圖表工具
* 透過簡單的指令可以完成一些我們在工程上會使用到的圖表
## 餅形圖(Pie Chart)
```mermaid
    pie 
    title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15 
```
## 流程圖（Flow Chart）

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
## 時序圖（Sequence Diagram）
```mermaid
sequenceDiagram
    autonumber
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->>John: Fight against hypochondria
    end
    Note right of John: Rational thoughts!
    John-->>Alice: Great!
    John->>Bob: How about you?
    Bob-->>John: Jolly good!
```
## 狀態圖(State Diagram)
```mermaid
stateDiagram
  [*] --> Still
  Still --> [*]
  Still --> Moving
  Moving --> Still
  Moving --> Crash
  Crash --> [*]
```
## 甘特圖（Gantt Diagram）
```mermaid
gantt
dateFormat  YYYY-MM-DD
title Adding GANTT diagram to mermaid
excludes weekdays 2014-01-10

section A section
Completed task            :done,    des1, 2014-01-06,2014-01-08
Active task               :active,  des2, 2014-01-09, 3d
Future task               :         des3, after des2, 5d
Future task2               :         des4, after des3, 5d
```

## 類圖(class Diagram)
```mermaid
classDiagram
      Animal <|-- Duck
      Animal <|-- Fish
      Animal <|-- Zebra
      Animal : int age
      Animal : String gender
      Animal: isMammal()
      Animal: mate()
      class Duck{
          String beakColor
          swim()
          quack()
      }
      class Fish{
          int sizeInFeet
          canEat()
      }
      class Zebra{
          bool is_wild
          run()
          eat()
      }
```
## 後記
* 如要在vscode中show出mermaid的圖形需下載補充軟體
* 輸入mermaid即可找到
## 參考資料
* [Include diagrams in your Markdown files with Mermaid](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)
* [在Markdown中用mermaid語法繪製圖表](https://www.gushiciku.cn/pl/pP3d/zh-tw)
