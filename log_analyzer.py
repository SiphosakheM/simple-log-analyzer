def analyzer_log(file_log , keywords):
    number_of_line = 0
    keywords_count = {keyword : 0 for keyword in keywords}
    try:
        with open(file_log , "r") as file:
            for line in file:
                number_of_line += 1
                for keyword in keywords:
                    if keyword in line:
                        keywords_count[keyword] += 1
    except "FileNotFoundError":
        print("ERROR: file not found")
        return 
    for keyword, count in keywords_count.items():
        print(f"'{keyword}' number of occurence: {count}")
        
file_log = "app.log"
keyword_in_keywords = ["ERROR", "CRITICAL", "WARNING", "FAILED"]
analyzer_log(file_log,keyword_in_keywords)