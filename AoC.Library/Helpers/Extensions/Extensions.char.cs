namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        public static int ToInt(this char value)
        {
            var result = (int)char.GetNumericValue(value);
            return result == -1
                ? throw new ArgumentException(value + " is not a numeric value")
                : result;
        }
    }
}
