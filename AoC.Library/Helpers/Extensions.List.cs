namespace AoC.Library.Helpers
{
    public static partial class Extensions
    {
        /// <summary>
        /// Literally <see cref="IList{T}.RemoveAt(int)"/> but returns the input list.
        /// </summary>
        public static IList<T> RemoveAtFluent<T>(this IList<T> list, int ix)
        {
            list.RemoveAt(ix);
            return list;
        }

        /// <summary>
        /// Pointless alias. Name just makes it more explicit.
        /// </summary>
        public static List<T> Copy<T>(this List<T> list) => new(list);
    }
}
