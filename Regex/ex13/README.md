# Regular expression in Python

## Understand the meaning

Figure out the meaning of given regular expressions. Feel free to use code or [online interpreter](https://extendsclass.com/regex-tester.html#python) to test your assumption.

In order to solve this exercise just explain the meaning together with an example below the given Regex.

### For example

([A-Z])\w+
Extracts words with a starting capital letter.
e.g.: Hello my name is Mathias --> matches "Hello" and "Mathias"

---

1. colou?r  
--> color or colour

2. (\W|^)[\w.\-]{0,25}@(gmail|deliveryhero)\.com(\W|$)  
--> emails with TLD gmail.com or deliveryhero.com

3. ^(?=.\*[a-z])(?=.\*[A-Z])(?=.\*\d).{6,12}$  
--> PW  
6 to 12 characters in length  
Must have at least one uppercase letter  
Must have at least one lower case letter  
Must have at least one digit  
Should contain other characters  


4. ^\#?([a-f0-9]{6}|[a-f0-9]{3})$  
--> hex color code  

5. done$  
--> a text that ends with "done"  
