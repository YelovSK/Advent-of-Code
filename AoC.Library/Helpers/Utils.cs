namespace AoC.Library.Helpers
{
    public static class Utils
    {
        /// <summary>
        /// Because declaring a variable inside try catch makes it annoying to use in the outer scope.
        /// </summary>
        /// <param name="result">Function result if success</param>
        /// <param name="defaultValue">Sets the default value of result</param>
        /// <returns>If is success (did not throw an exception)</returns>
        public static bool TryRun<T>(Func<T> func, out T? result, T? defaultValue = default)
        {
            try
            {
                result = func();
                return true;
            }
            catch
            {
                result = defaultValue;
                return false; 
            }
        }
    }
}
