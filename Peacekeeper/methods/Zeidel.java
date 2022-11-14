package com.company.Peacekeeper.methods;

import com.company.Peacekeeper.objects.Function;

import java.util.HashSet;
import java.util.Set;

public class Zeidel {

    public static Set<Double> run(Function function1, Function function2, double x0, double y0, double eps) {
        double tempX = x0, lastX;
        double tempY = y0, lastY;
        double check;


        if (!convergenceIs(tempX, tempY, function1, function2)) {
            System.out.println("Условие сходимости не выполняется");
            System.exit(0);
        }

        do {
            lastX = tempX;
            lastY = tempY;
            tempX = function1.getValueIn(lastX, lastY);
            tempY = function2.getValueIn(tempX, lastY);
            check = Math.max(Math.abs(function1.getValueIn(tempX, tempY) - function1.getValueIn(lastX, lastY)),
                    Math.abs(function2.getValueIn(tempX, tempY) - function2.getValueIn(lastX, lastY)));
        } while (check > eps);

        Set<Double> ans = new HashSet<>();
        ans.add(tempX); ans.add(tempY);

        return ans;
    }

    public static boolean convergenceIs(double x0, double y0, Function func1, Function func2) {
        double checkX = Math.abs(func1.getFirstDifferentiateIn(x0, y0, "x")) +
                Math.abs(func2.getFirstDifferentiateIn(x0, y0, "x"));

        double checkY = Math.abs(func1.getFirstDifferentiateIn(x0, y0, "y")) +
                Math.abs(func2.getFirstDifferentiateIn(x0, y0, "y"));

        return checkX <= 1 || checkY <= 1;
    }

}