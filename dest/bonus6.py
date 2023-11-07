contents = ["All carrots are to be sliced longitudinally.",
            "The carrots where repotedly sliced.",
            "The slicing process as well present"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
    file.close()
