namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        public static bool ToBool(this int value) => value switch
        {
            0 => false,
            1 => true,
            _ => throw new ArgumentException(),
        };
    }
}
