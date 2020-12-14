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
*  0 Echo Reply: 查詢
*  3 Destination Unreachable:錯誤
*  4 Source Quench:錯誤
*  5 Redirect:錯誤
*  8 Echo Request:查詢
* 11 Time Exceeded:錯誤
* 12 Parameter Problem:錯誤
* 13 Timestamp Request:查詢
* 14 Timestamp Request:查詢
* 15 Information Reply:查詢
* 16 Information Reply:查詢
* 17 Address Mask Request:查詢
* 18 Address Mask Reply:查詢
### 無法抵達目的節點原因
*  0 目的端網路無法連接
*  1 目的端主機無法連線
*  2 指定通訊協定不存在
*  3 指定連接阜不存在
*  4 資料需被分隔並設定不可分割位元
*  5 來源選擇路徑失敗
*  6 目的端網路無法辨識
*  7 目的端主機無法辨識
*  8 來源端主機被隔離
*  9 禁止與目的端網路通訊
* 10 禁止與目的端主機通訊
* 11 無法連接此網路服務類型
* 12 無法連接此主機服務類型
* 13 被過濾禁止通訊
* 14 違反主機優先權
* 15 優先權實行中斷
