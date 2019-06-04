#23 Makes use of languages.txt
#Harder exercise, mostly copying here, not sure what he's going for.

#Another way to import modules/features.
#importing this way is more verbose, as you'd have to type module name
#before the specific feature.
import sys
scriptName, encoding, error = sys.argv

#I guess this is the main method, similar to Java?
def main(language_file, encoding, errors):

    line = language_file.readline()
    #if the line exists, then we can proceed, otherwise skip.
    if line:
        print_line(line,encoding,errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #strip removes the \n at the end of the readline
    next_lang = line.strip()
    #encode into raw bytes.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #decode into a real python string.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)

#In order to be able to decode any given raw bytes string the way we did here,
#We need a rawbytes in the form of rawBytes = b'\xa3\xb2' <- Example
#Using encode() on a utf string, we get raw bytes.
#DBES => Decode Bytes, Encode Strings.
