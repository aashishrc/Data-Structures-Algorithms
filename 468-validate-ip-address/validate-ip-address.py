class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if ':' in queryIP:
            #implementation of ipv6
            subnets = queryIP.split(':')
            if len(subnets) == 8:
                for i in subnets:
                    if len(i) <= 4 and len(i) >= 1:
                        print(i)
                        for j in i.lower():
                            if 'a' <= j <= 'f' or '0' <= j <= '9':
                                continue
                            # if ord(j) >= 48 and ord(j) <= 57 or ord(j) >= 97 and ord(j) <= 102:
                            #     continue
                            else:
                                return "Neither"
                    else:
                        return "Neither"
                return "IPv6"
            return "Neither"
        else:
            #ipv4
            subnets = queryIP.split('.')
            if len(queryIP) > 15:
                return "Neither"
            if len(subnets) == 4:
                for i in subnets:
                    if not i.isdigit() or not int(i) >= 0 or not int(i) <=255 or str(int(i)) != i:
                        return "Neither"
                    #add condition to check for leading zeroes
                return "IPv4"
            return "Neither"
            