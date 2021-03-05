# CentOS7第二週學習筆記
## 前言
* 本週在執行yum時發生黑頻死機方面的問題，故更換iso重新下載 (CentOS-7-x86_64-DVD-2009.iso)
## 安裝過程
![1](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-1.PNG)
![2](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-2.PNG)
## 指令對照
 Windows | Linux | notes
 -----|-----------|-------
 ipconfig | ifconfig | 顯示網路連線之設定
 route print | ip route show | 秀出路由表
## 觀念
* 網路位址轉換 Network Address Translation，縮寫：NAT；又稱網路掩蔽、IP掩蔽:<br>
在計算機網路中是一種在IP封包通過路由器或防火牆時重寫來源IP地址或目的IP位址的技術。<br>
這種技術被普遍使用在有多台主機但只通過一個公有IP位址存取網際網路的私有網路中。<br>
內部連的到外部VM->Internat(o)(ex:Linux ping 192.196.60.1)<br>
外部連不到內部Internat->VM(x)(ex:window ping 10.0.2.2)
## 指令操作
![3](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-3.PNG)
>sudo ifconfig ens33 0 ------>讓ens33的ip變成0 
---
![4](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-4.PNG)
>sudo ifconfig ens33 ------->讓ens33的ip變成上圖之ip
---
![5](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-5.PNG)
>再利用clone的虛擬機進行改ip及ping該ip確認是否成功
---
![6](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-6.PNG)
>sudo yum install openssh-server
---
![7](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-7.PNG)
>利用clone後的linux系統進行登入，在此步驟前筆者原無設定RichChen的password會有不知密碼無法登入的問題，設定完後便可解決!
---
![8](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-8.PNG)
>利用本機進行登入
---
![9](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-9.PNG)
>安裝Winscp並登入
---
![10](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-10.PNG)
>將helloworld.txt這個檔案傳到RickChen中
---
![11](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-11.PNG)
>helloworld中的內容
---
![12](https://github.com/cycyucheng1010/NQU/blob/main/Centos7/week2-12.PNG)
>傳送後多了helloworld.txt之檔案，利用cat開啟後可發現內文符合!說明傳送成功且正確
---
## 參考資料
* [CentOS-xxxx-LiveCD.ios 和CentOS-xxxx-bin-DVD1.iso有什麼區別？](https://www.itread01.com/content/1546347788.html)
* [安裝 CentOS7.x 鳥哥](http://linux.vbird.org/linux_basic/0157installcentos7.php)
* [Linux命令 vim及cat](https://www.itread01.com/content/1545716826.html)
* [full clone vs linked clone](https://www.vmware.com/support/ws5/doc/ws_clone_typeofclone.html)
