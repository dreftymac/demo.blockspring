import blockspring
import jinja2
import textwrap
import yaml

def barebones_jinja():
  objinja   = yaml.load('''
  ### ------------------------------------------------------------------------
  __dataconfig__:
    main:
      noop: x
    project_name:     barebones jinja2 demo
    project_desc:     Learn X in Y minutes
    project_url:      "https://github.com/adambard/learnxinyminutes-docs"
    list_of_colors:
      - red
      - orange
      - yellow
      - green
      - blue
      - indigo
      - violet
    dictionary_of_places:
      New York:
        Capital: Albany
      California:
        Capital: Sacramento
      France:
        Capital: Paris
    table_of_datarows:
      - {"alpha":one, "bravo":two, "charlie":three, }
      - {"alpha":uno, "bravo":dos, "charlie":tres,  }
      - {"alpha":ein, "bravo":swei, "charlie":drei, }
  ### ------------------------------------------------------------------------
  __template001__: |
    {# this is a comment #}
    
    Hello {{main.age}} year old {{main.fname}}!
    
    {% for color in list_of_colors %}<a href="https://duckduckgo.com/?q={{color}}&ia=meanings">{{color}}</a>{% endfor %}
    
  ''')
  return objinja
##enddef

def block(request, response):
  ##
  vout      = ''
  
  ##
  name      = request.params["first_name"]
  age       = str(request.params["age"])
  
  ##
  objinja   = barebones_jinja()
  objinja['__dataconfig__']['main']['fname']      = name
  objinja['__dataconfig__']['main']['age']        = age
  
  ##
  oEnv      =   jinja2.Environment()
  
  ## render
  template  =   oEnv.from_string(textwrap.dedent(objinja['__template001__']))
  vout      =   template.render(objinja['__dataconfig__'])
  
  ##
  response.addOutput(vout)
  response.addOutput("html", vout)
  response.end()
##enddef

blockspring.define(block)

