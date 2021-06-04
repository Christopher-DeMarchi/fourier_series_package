def graphing_summations(Length,Sum_of_Harmonics,Const,Function):
    '''Graphs summations on the x y plane
    Takes the inputs of the length, harmonic, constants, and the function
    Needs the following libraries
     ''' 
    Domain = np.linspace(-Length,Length,50)
    ao = np.ones((x.size),dtype = float) #Creates array of 1s to be filled
    Function = Const*ao # Fills in array with the constants
    
    for n in range(1,Sum_of_Harmonics,1):
        Function = Function + ((4*(-1)**n) / n**2)*np.cos(n*x)
    
    plt.plot(Domain,Function)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Summation Graph')
    plt.show()