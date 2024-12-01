namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        public static IEnumerable<string> SplitLines(this string input)
        {
            return input.Split(Environment.NewLine)
                        .Select(line => line.Trim());
        }

        public static IEnumerable<string> SplitWords(this string input)
        {
            return input.Split([' '], StringSplitOptions.RemoveEmptyEntries);
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
