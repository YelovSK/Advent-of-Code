using System.Data;

namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        public static IEnumerable<string> SplitLines(this string input)
        {
            return input.Split(Environment.NewLine, StringSplitOptions.RemoveEmptyEntries)
                        .Select(line => line.Trim());;
        }

        public static IEnumerable<string> SplitWords(this string input)
        {
            return input.Split([' '], StringSplitOptions.RemoveEmptyEntries);
        }

        public static IEnumerable<(Position position, char c)> GetGridPositions(this string input)
        {
            var lines = input.SplitLines().ToList();

            for (var y = 0; y < lines.Count; y++)
            {
                for (var x = 0; x < lines[y].Length; x++)
                {
                    var c = lines[y][x];
                    yield return (new Position(x, y), c);
                }
            }
        }

        public static Size GetGridSize(this string input)
        {
            var lines = input.SplitLines().ToList();
            return new Size(lines.First().Length, lines.Count);
        }

        #region I hate typing {type}.Parse

        public static int ToInt(this string input)
        {
            return int.Parse(input);
        }

        public static long ToLong(this string input)
        {
            return long.Parse(input);
        }

        public static decimal ToDecimal(this string input)
        {
            return decimal.Parse(input);
        }

        public static float ToFloat(this string input)
        {
            return float.Parse(input);
        }

        #endregion
    }
}
