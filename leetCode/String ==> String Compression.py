class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        write_index = 0  # Index to write the compressed characters
        read_index = 0   # Index to iterate through the original characters

        while read_index < len(chars):
            char = chars[read_index]
            count = 0

            # Count the consecutive occurrences of the current character
            while read_index < len(chars) and chars[read_index] == char:
                read_index += 1
                count += 1

            # Write the character to the compressed array
            chars[write_index] = char
            write_index += 1

            # If the count is greater than 1, write the count as characters
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
