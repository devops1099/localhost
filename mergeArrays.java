

import java.util.Arrays;
 
public class mergeArrays
{
    private static int[] mergeArray(int[] arrayA, int[] arrayB)
    {
        int[] mergedArray = new int[arrayA.length + arrayB.length];
         
        int i=0, j=0, k=0;
         
        while (i < arrayA.length && j < arrayB.length)
        {
            if (arrayA[i] < arrayB[j]) 
            {
                mergedArray[k] = arrayA[i];
                i++;
                k++;
            } 
            else
            {
                mergedArray[k] = arrayB[j];
                j++;
                k++;
            }
        } 
                 
        while (i < arrayA.length) 
        {
            mergedArray[k] = arrayA[i];
            i++;
            k++;
        } 
                 
        while (j < arrayB.length) 
        {
            mergedArray[k] = arrayB[j];
            j++;
            k++;
        } 
             
        return mergedArray;
    }
     
    public static void main(String[] args) 
    {
        int[] A = new int[] {7, 12, 29, 41, 56, 79};
         
        int[] B = new int[] {19, 36, 52, 99};
         
        int[] resArray = mergeArray(A, B);
         
        System.out.println("Array B : "+Arrays.toString(A));         
        System.out.println("Array B : "+Arrays.toString(B));
        System.out.println("Merged Array : "+Arrays.toString(resArray));
    }
}