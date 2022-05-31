from jinja2 import Environment, FileSystemLoader , StrictUndefined
#Local Directory
file_loader = FileSystemLoader('.')
#Load Environment
env = Environment(loader=file_loader)

#There is two templates for now , we comment out based if we need a spine of leaf config output
### Rack Template
template = env.get_template('nat.j2')
from nat import data
#Dictionary that contains Variables to populate the template files

def render_cfg():
    #Opens the host device dictionary and pulls the values
    #hostname = (data['device']['hostname'])
    #This will take the hostfile file variables and run through the jinja2 file and output a yaml file
    leaf_config = template.render(data, undefined=StrictUndefined)
    #Create the leaf yaml file
    #leaf_file = hostname+"yml"


    #with open(leaf_file, 'w+') as leafcfg:
    #    leafcfg.write(leaf_config)
    #    leafcfg.close()

    #Print the output
    print(leaf_config)


if __name__ == "__main__":
    render_cfg()
