import re
class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        # Regex pattern for validating IPv4
        ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}'
                                r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
        
        # Regex pattern for validating IPv6
        ipv6_pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

        if ipv4_pattern.match(queryIP):
            return "IPv4"
        elif ipv6_pattern.match(queryIP):
            return "IPv6"
        else:
            return "Neither"

# # Example usage:
# print(validIPAddress("192.168.1.1"))       # Output: IPv4
# print(validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: IPv6
# print(validIPAddress("192.168.01.1"))      # Output: Neither
# print(validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")) # Output: Neither

        