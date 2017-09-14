#
# Browser Interactions
#
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# Python standard libraries
import time
#
# The selenium wrapper class contains two main functions that remove the need to specify whether
# the selector is a css selector or a xpath.
#
class SeleniumWrapper:
	def __init__(self):
		self.html_tags = ["a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "blockquote", "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", "details", "dfn", "dialog", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", "keygen", "label", "legend", "li", "link", "main", "map", "mark", "menu", "menuitem", "meta", "meter", "nav", "noscript", "object", "ol", "optgroup", "option", "output", "p", "param", "pre", "progress", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp", "script", "section", "select", "small", "source", "span", "strong", "style", "sub", "summary", "sup", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr"]
		self.driver = None
	def get_element(self, selector, father = None):
		father = self.driver if father == None else father
		if selector == "":
			return father
		elif (selector[0] == '.' and './/' not in selector) or selector[0] == '#' or selector in self.html_tags:
			return father.find_element_by_css_selector(selector)
		else:
			return father.find_element_by_xpath(selector)
	def get_elements(self, selector, father = None):
		father = self.driver if father == None else father
		if selector == "":
			return [father]
		elif (selector[0] == '.' and './/' not in selector) or selector[0] == '#' or selector in self.html_tags:
			return father.find_elements_by_css_selector(selector)
		else:
			return father.find_elements_by_xpath(selector)
class FacebookInteractions(SeleniumWrapper):
   def __init__(self, driver = None):
     SeleniumWrapper.__init__(self)
     self.driver = driver or webdriver.Firefox()
   def login(self, username, password):
     self.driver.get('http://www.facebook.com')
     time.sleep(2)
     self.get_element('#email').send_keys(username)
     time.sleep(2)
     self.get_element('#pass').send_keys(password)
     time.sleep(2)
     self.get_element('#pass').submit()
     return True
if __name__=="__main__":
  page = FacebookInteractions()
  page.login("your_username", "your_password")