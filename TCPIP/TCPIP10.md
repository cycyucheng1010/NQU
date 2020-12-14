# TCP/IP_CH10
## ARP(Address Resolution Protocol)
### 簡介
*將IP位址映射為實體位址
IP Address----->Physical Address
* 資料傳送前對照ARP對照表
## RARP(Reversed Address Resolution Protocol)
### 簡介
* 來源端知道自己的MAC位址，但不知道IP
Physical Address---->IP Address
* 發生在沒有磁碟機或終端機的設備(無法進行IP儲存)
## ICMP(Internet Control Message Protocol)
### 簡介
* ICMP屬於網路層的通訊協定
* 常用指令: ping , tracert
* Echo Request/Reply:目的端收到後回傳指定訊息
### ICMP訊息
* 0 Echo Reply: 查詢
* 3 Destination Unreachable:錯誤
* 4 Source Quench:錯誤
* 5 Redirect:錯誤
