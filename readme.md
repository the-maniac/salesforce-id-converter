#SalesForce id converter

Function for convert SalesForce id from case sensitive 15 chars, to case insensitive 18 chars id. 
Base on these articles [1](https://astadiaemea.wordpress.com/2010/06/21/15-or-18-character-ids-in-salesforce-com-%E2%80%93-do-you-know-how-useful-unique-ids-are-to-your-development-effort/) [2](http://salesforce.stackexchange.com/questions/27686/how-can-i-convert-a-15-char-id-value-into-an-18-char-id-value/27694)

_example:_

`>> print convert_id_15_to_18('001A000010khO8J')`

`>> 001A000010khO8JIAU`
