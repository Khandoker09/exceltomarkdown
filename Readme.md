
# How to Build

This repo contain 2 python file which can add excel spread sheet value to a markdown file automatically.
Using pandas we can easily load a excel file. After some processing the spread sheet data devided into 5 diffrent table then all those table will be saved in .txt file.
add_table.py file will can add those table to a specific markdown file. In mardown file there should be a reference line after that reference line we will add the table .
pandas to markdown function was used to convert the table in a markdown formats .




```

wiki.to_markdown(r"C:\Users\USER\Desktop\wiki.txt",index=False)



```
