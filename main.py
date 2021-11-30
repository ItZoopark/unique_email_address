def numUniqueEmails(emails):
    email_set = set()
    for email in emails:
        domain_start_pos = email.rfind('@')
        local_name = email[:domain_start_pos]
        if local_name.find('+') != -1:
            ignore_from_pos = local_name.find('+')
            local_name = local_name[:ignore_from_pos]
        email_res = local_name.replace(".", "") + email[domain_start_pos:]
        email_set.add(email_res)
    return len(email_set)


def numUniqueEmails2(emails):
    email_list = []
    for email in emails:
        domain_start_pos = email.rfind('@')
        local_name = email[:domain_start_pos]
        if local_name.find('+') != -1:
            ignore_from_pos = local_name.find('+')
            local_name = local_name[:ignore_from_pos]
        email_res = local_name.replace(".", "") + email[domain_start_pos:]
        if email_res not in email_list:
            email_list.append(email_res)
    return len(email_list)


def numUniqueEmails3(emails):
    email_list = set()
    for email in emails:
        mas = email.split('@')
        local_name = mas[0].replace('.', '').split('+')[0]
        domain = mas[1]
        res = local_name + '@' + domain
        email_list.add(res)
        # if res not in email_list:
        #     email_list.append(res)
    return email_list


# emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.catchy@leetcode.com", "testemail+david@lee.tcode.com"]
# emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
print(numUniqueEmails(emails))
