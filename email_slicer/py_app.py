def email_slicer():
    user_email = input("Type your email: ")
    (username, domain) = user_email.split("@")
    (domain, extension) = domain.split(".")
    print(username  + "\n" + domain + "\n" + extension)

email_slicer()