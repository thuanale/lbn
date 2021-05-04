1. page 
1.1 main page
-> check/download wedriver
- check login
-> check your Keyboard input or your Unicode language 

1.2 Welcome page
1.3 Tape page
1.4 Advanced Search Page

2. Advanced Search
Hover menu id: ctl09_3
Advanced search: ctl09_3_2
3. Drop down menu:
ddlFields:
option: Alternate Code

ddlOperators:
option: value=SUBSTRING.

4. Loop
Until End-Of-Line:
txtMultipleEdit:
> get value from txt file
(get column w/ tape number [4-5][0-9]{5})
> send to tape
btnAddMultiple:
> click()

btnSubmit

Alternate code order:
gridPageuwg_c_0_2
> click()

6. Search & return result
- sort
- unselected all
- check duplicate tape:
	find list of tape contains duplicated tape:
		quantity = [] => new.append('tape')
		quantity = 1  => ok
		quantity > 1	=> 
		
	get smallest
- remove all selected.

check movement = offsite/retrieved:
 offsite:
	> RD1066C? => pickup
 return:
	kddi/ntt
	RD1005C? RD1066C? order in different batch

loop:	
- selected:
> RD1005C: play order.
> RD1066C: play order/pickup.

- order: 
> download the file
> return to tape

7. do you one to try another list?
yes:
clear all & start from stop 3