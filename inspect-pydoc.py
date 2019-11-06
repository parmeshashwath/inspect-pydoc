import inspect
import funcsigs
import pymongo

def getmarkdown(module):
    output = [ "*"*100 ]
    output.extend(getfunctions(module))
    output.append("***\n")
    # print(output)
    output.extend(getclasses(module))
    return "\n".join(output)


def getclasses(item):
    output = list()
    for cl in inspect.getmembers(item, inspect.isclass):
        if cl[0] != "__class__" and not cl[0].startswith("_"):
            # Consider anything that starts with _ private
            # and don't document it
            output.append( "#"*100 )
            output.append(cl[0])   
            # Get the docstring
            output.append(inspect.getdoc(cl[1]))
            # Get the functions
            output.extend(getfunctions(cl[1]))
            # Recurse into any subclasses
            output.extend(getclasses(cl[1]))
    return output



def getfunctions(item):
    output = list()
    for func in inspect.getmembers(item, inspect.isfunction):
        output.append( "@"*100 )
        output.append(func[0])
       
        output.append("\n")
         # Get the signature
        output.append(str(inspect.signature(func[1]))) ## funcsigs.signature(func[1]) for python 2.7
        # Get the docstring
        if inspect.getdoc(func[1]):
            output.append("DocString: " + inspect.getdoc(func[1]))
        else:
            output.append("No docstring.")
    return output




if __name__ == '__main__':
    
    doc = getmarkdown(pymongo)
    with open("sample_doc.md",'w') as f:
        f.write(doc)