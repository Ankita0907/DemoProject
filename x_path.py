'''
XPath (XML Path Language) in Selenium with Python is a powerful technique used to locate elements on a webpage using XML-like syntax.
XPath is especially useful when other locators (like ID, class name, etc.) are not available or practical to use.
XPath Basics:
XPath expressions can be absolute or relative:

Absolute XPath: Starts from the root node (/html/body/div[1]/div[2]/form/input)
Relative XPath: Starts from the current node (e.g., //form/input)

Different Types of XPath in Selenium with Python:
1) Absolute XPath: Begins with a single forward slash / and provides the complete path from the root element to the desired element.
2) Relative XPath: Starts with a double forward slash // and allows searching for elements anywhere on the webpage, not necessarily starting from the root.
3)XPath Axes: Allows navigating elements relative to their position in the DOM tree.
Examples of Axes:

child: Selects direct child elements.
SYNTAX-  xpath_child = "//div[@id='parent']/child::div"

descendant: Selects all descendants of the current node.
SYNTAX-  xpath_descendant = "//div[@id='parent']/descendant::input"

parent: Selects the parent of the current node.
SYNTAX- xpath_parent = "//input[@id='child']/parent::form"

4) XPath Predicates:
Used to find elements based on conditions like attribute values or text content.
Examples of Predicates:
Selecting an element with a specific attribute:     xpath_attribute = "//input[@type='text']"

xpath_text = "//div[contains(text(),'Welcome')]"

5)XPath Functions: Provides functions for more complex selections.
Examples of Functions:
  text(): Selects elements based on their text content
SYNTAX-    xpath_text_function = "//button[text()='Submit']"

  contains(): Checks if an attribute or text contains a specific value.
SYNTAX-   xpath_contains_function = "//div[contains(@class, 'container')]"

6) XPath Operators: Allows combining conditions and expressions.
Examples of Operators:
Combining multiple conditions-:   xpath_multiple_conditions = "//input[@type='text' and @name='username']"






'''