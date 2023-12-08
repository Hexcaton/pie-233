import re
def extract_domains(emails):
    pattern = re.compile(r'@([a-zA-Z0-9.-]+)')
    domains = [re.search(pattern, email).group(1) for email in emails if re.search(pattern, email)]
    return domains

email_list = ['user1@example.com', 'user2@gmail.com', 'user3@yahoo.com']
result_domains = extract_domains(email_list)
print(result_domains)