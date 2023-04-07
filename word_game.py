"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys


class PlayerWords:
    """PlayerWords is a class that reads a player's list of words from a file 
    and calculate two players' score for a fictional word game.
    
    Attributes:
        words(set): A set of strings containing the unique words found by the 
        player.
    """
    
    def __init__(self, file_path):
        """Method that initializes a PlayerWords object with a set of words 
        from a text file.
        
        Args:
            file_path (str): A string containing the path to a text file.
        
        Side effects:
            Reads in words from the file and stores them as a set in the words 
            attribute.
        """
        # Initialize an empty set to store the words
        self.words = set()
        # Open the file and read in each word, stripping whitespace
        with open(file_path, 'r', encoding = "utf-8") as f:
            for line in f:
                word = line.strip()
                self.words.add(word)

    def score(self, PlayerWords):
        """Method that calculates the score for the team consisting of the 
        player and their other_player
        
        Args:
            PlayerWords (PlayerWords): Another PlayerWords object representing 
            the words found by the partner.
        
        Returns:
            points (int): The total score for the team.
        """
        points = 0
        same_words = self.words.intersection(PlayerWords.words)
        for word in same_words:
            if len(word) >= 3:
                points += len(word) - 2
        return points


def main(file_path1, file_path2):
    """Function that reads in two sets of words from text files, creates 
    PlayerWords objects for each player, computes their team's score for a word 
    game, and shows it to the console.
    
    Args:
        file_path1 (str): A string containing the path to a text file 
        containing the words found by player 1.
        file_path2 (str): A string containing the path to a text file 
        containing the words found by player 2.
    
    Side effects:
        Prints the team's score to the console.
    """
    # Create PlayerWords objects for each player
    player1 = PlayerWords(file_path1)
    player2 = PlayerWords(file_path2)
    # Compute the team's score using player1's words and print it to the console
    team_score = player1.score(player2)
    print(f"Your team scored {team_score} points!")


def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
