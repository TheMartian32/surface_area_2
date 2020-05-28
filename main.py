from math import pi

"""
=========================================================
A script to calculate the surface area of a given object.
=========================================================

Returns:
    Floats/Strings/Integers -- Based off the user input answers, it gives floats, integers, or  strings.
"""


class repeat_question():
    def ask_for(self, prompt, error_msg=None, _type=None):
        """ While the desired prompt is not given, it repeats the prompt. """
        while True:
            inp = input(prompt).strip()
            if not inp:
                if error_msg:
                    print(error_msg)
                continue

            if _type:
                try:
                    inp = _type(inp)
                except ValueError:
                    if error_msg:
                        print(error_msg)
                    continue
            return inp

    def round_num(self, num=0):
        need_to_round = co.ask_for(
            'Do you want to round? (Y/N): ', 'Not an answer', str)
        if need_to_round[0] == 'Y':
            digits_after = co.ask_for(
                'How many digits do you want after the decimal point?: ', '\nWont work', int)
            return print(round(num, digits_after))
        else:
            pass


# * Creates an instance of the repeat_question class
co = repeat_question()

#===============================================================================================#


class calc():

    def __init__(self):
        pass

    # * Calculations below:

    def rect_prism(self):
        """Calculates  the surface area of a rectangular prism.

        Returns:
            Float/Integer -- Based on user input values, returns surface area.
        """
        result = ''
        print('\n----------------------------')
        h = co.ask_for('Please enter the height:  ',
                       'Not an integer/float.', float)
        l = co.ask_for('Please enter the length: ',
                       'Not an integer/float.', float)
        w = co.ask_for('Please enter the width: ',
                       'Not an integer/float.', float)
        print('----------------------------')
        # * Calculation:
        calculation = 2*w*l+2*h*l+2*h*w

        return print(f'\nThe surface area is {calculation}.')
    # ? Kinda works, somewhat off on the decimal point, don't really know how to fix it.
    #! ORDER MATTERS. Can be inaccurate if the parameters weren't put in right.

    def tri_prism(self):
        """
        Takes in user inputted values then calculates the surface
        area based on those values

        Returns:
            [Float/Int] -- Returns a surface area thats either an integer or floating point
        """

        result = ''
        print('\n----------------------------')
        print('\nIMPORTANT:')
        print('Carefully analyze the numbers you input to the questions, inputting the same numbers in a different order can yield a much different, often inaccurate result')
        triangle_height = co.ask_for(
            '\nPlease enter the  height of the triangle: ', 'Not a height', float)
        trianlge_base = co.ask_for(
            'Please enter the base length of the triangle: ', 'Not a triangle length', float)
        height = co.ask_for('Please enter the height:  ',
                            'Not an integer/float.', float)
        lateral_base = co.ask_for('Please enter the base side: ',
                                  'Not an integer/float.', float)
        lateral_base2 = co.ask_for('Please enter the lateral side: ',
                                   'Not an integer/float.', float)
        lateral_base3 = co.ask_for('Please enter the lateral side: ',
                                   'Not an integer/float.', float)
        print('----------------------------')

        # * Calculations

        # triangle part of triangular prism
        a = triangle_height*trianlge_base
        a = a/2

        # lateral sides part
        l1 = lateral_base*height
        l2 = lateral_base2*height
        l3 = lateral_base3*height

        s_calc = a+a+l1+l2+l3

        return print(f'\nThe surface area is {s_calc}.')

    def rect_pyramid(self):
        """Calculates the surface area of a rectanagular pyramid based off user inputted values

        Returns:
            Float/Int -- Returns a surface area thats either an integer or floating point.
        """

        result = ''
        print('\n----------------------------')
        base = co.ask_for('What is the base length?: ',
                          'Not a supported type.', float)

        height = co.ask_for('What is the lateral face length?: ',
                            'Not a supported type.', float)
        print('----------------------------')

        # * Calculations

        # Base of rectangular pyramid
        base_area = base*base

        # Side triangle area
        lateral_area = base*height/2

        # * Surface area
        surf_area = base_area + lateral_area*4

        return print(f'\nThe surface area is {surf_area}')

    def tri_pyramid(self):
        """Calculates the surface area of a triangular prism

        Returns:
            Float/Int -- Returns a surface area thats either an integer or floating point.
        """

        result = ''
        print('\n----------------------------')
        base = co.ask_for('What is base length?: ',
                          'Not a supported type.', float)

        base_height = co.ask_for(
            'What is the base height?: ', 'Not a supported type', float)

        height = co.ask_for('What is lateral face height?: ',
                            'Not a supported type.', float)
        print('----------------------------')

        # * Calculations

        # Base area of triangular pyramid
        base_area = base*base_height/2

        # Lateral triangle area
        lateral_area = base*height/2

        # * Surface area
        surf_area = base_area + lateral_area*3

        return print(f'\nThe surface area is {surf_area}')

    def cyl(self):
        #! Somewhat inaccurate, not ready for use.
        """Calculates the surface area of a cylinder based off of user inputted values

        Returns:
            Float/Int -- Returns the surface area thats either an integer of floating point.
        """

        result = ''
        print('\n----------------------------')
        lateral_included = co.ask_for(
            'Are you using the lateral faces in this calculation?: ', 'Not an answer', str)

        radius = co.ask_for('What is the radius?: ', 'Not a radius.', float)

        height = co.ask_for('What is the height?: ', 'Not a height', float)
        print('----------------------------')

        # * Calculations below

        # * Formula: 2pi*r^2 + 2pi*rh

        # Base area of cylinder
        base_area = 2*radius**2

        # Lateral area of cylinder
        lateral_area = 2*radius*height

        # * Surface area
        surf_area = lateral_area+base_area
        surf_area = surf_area*3.14

        if lateral_included in ['n', 'no', 'nyet']:
            surf_area = lateral_area*pi
            return print(f'The surface area is {surf_area}.')

        answer = round(surf_area, 2)

        return print(f'\nThe surface area of the cylinder is {answer}.')

#===============================================================================================#

    # * User inputs below:

    def calc_type(self):
        """Basically this method asks the user what type of calculation they will  be making
           e.g, surface area, addition, subtraction, all that jazz. Then based on that info,
           it calls certain methods, such as the rectangular surface area method for rectangular prisms.
        """
        # * Keeps asking the user  what calculation(s) they will be making until they answer, then calls the appropriate method.
        while True:
            result = co.ask_for('\nWhat type of calculation are you making?: ',
                                'Not a supported calculation type.', str)

            # * Surface  Area
            if result in ['surface area', 'surface', 'area']:
                area_type = ''
                print('\n----------------------------')
                area_type = co.ask_for(
                    'What type of surface area?: ', 'Not supported.', str)
                print('----------------------------')

                # * Rectangular Prism
                if area_type in ['rectangle', 'rect', 'r']:
                    c.rect_prism()
                    break

                # * Triangular Prism
                if area_type in ['t', 'triangle', 'triangular prism']:
                    c.tri_prism()
                    break

                # * Rectangular Pyramid
                if area_type in ['p', 'pyramid', 'rectangular pyramid']:
                    c.rect_pyramid()
                    break

                # * Triangular Pyramids
                if area_type in ['tp', 'triangular prism', 'tri pyr']:
                    c.tri_pyramid()
                    break

                # * Cylinder
                if area_type in ['c', 'cylinder', 'cl', 'cy']:
                    c.cyl()
                    break
            else:
                print('Not currently supported calculation type.\n')


#===============================================================================================#

c = calc()

if __name__ == "__main__":
    # * Calls the calculation type method to determine what calculation will be made
    # * and then asks if it can repeat the script if they need it.
    c.calc_type()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        repeat = input(
            '\nWould you like to repeat the program? (Y/N): ').lower()
        if repeat[0] == 'y':
            c.calc_type()
            continue
        if repeat[0] == 'n':
            break

#===============================================================================================#
