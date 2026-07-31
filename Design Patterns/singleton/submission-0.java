static class Singleton {

    private static volatile Singleton uniqueInstance = null;
    private String value = null;

    private Singleton() {

    }

    public static Singleton getInstance() {
        if (uniqueInstance == null) {
            synchronized(Singleton.class) {
                if (uniqueInstance == null) {
                    uniqueInstance = new Singleton();
                }
            }
        }

        return uniqueInstance;

    }

    public String getValue() {
        return value;

    }

    public void setValue(String value) {
        this.value = value;

    }
    
}
