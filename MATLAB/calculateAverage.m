% calculateAverage - Calculates the average of a numeric array.
%   This function takes a numeric array as input and returns 
%   the average of its elements. If the input is empty, the help text
%   here is returned. All functions should have a short introduction, in
%   layman speak, of what the function does. Keep the lines short as well,
%   as much is done in a terminal, and word-wrapping is new, old things
%   will make a user scroll, and no one likes that.
%
%   Always put the author and date, so you get credit (blame) and we know
%   the last time the code was updated. Not everything is in GitHub
%   history.
%   
%   BY: Jared Brzenski
%
%   Last Update: 2025-06-06
%
%   Give an strict usage example  of how to use your cool function.
%
%   Usage:
%   averageValue = calculateAverage( numericArray )
%
%   Input Arguments:
%   - numericArray (float): An array of values to take the mean of
%
%   Output Arguments:
%   - averageValue (float): The calculated average. Sometimes it is nice
%                           to also return the 'type' of value returned. 
%                           It may not make a difference here, but for
%                           some languages, especially FORTRAN, keeping
%                           track is important!
%
%   It is also nice to give an example of usage, just in case it is not
%   super obvious, or if your function takes cool inputs, that may not
%   be obvious from first glance. This function is kinda boring.
%   Example 1 - Calculate the average of a simple array::
%   % data = [1, 2, 3, 4, 5];
%   % avg = calculateAverage(data);
%   % disp(avg);
%
%
% See also MATLAB built in functions: sum, mean, std.

function averageValue = calculateAverage(numericArray)

    % Check if the input array is empty
    if isempty(numericArray)
        help averageValue
        return
    else
        % Calculate the sum of the elements
        totalSum = sum(numericArray);

        % Calculate the number of elements
        numElements = numel(numericArray);

        % Calculate the average
        averageValue = totalSum / numElements;
    end

end
