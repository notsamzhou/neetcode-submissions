interface Observer {
    void notify(String itemName);
}

class Customer implements Observer {
    private String name;
    private int notifications;

    public Customer(String name) {
        this.name = name;
        this.notifications = 0;
    }

    public void notify(String itemName) {
        this.notifications += 1;
    }

    public int countNotifications() {
        return this.notifications;
    }
}

class OnlineStoreItem {
    private String itemName;
    private int stock;
    private List<Observer> observers = new ArrayList<Observer>();

    public OnlineStoreItem(String itemName, int stock) {
        this.itemName = itemName;
        this.stock = stock;
    }

    public void subscribe(Observer observer) {
        observers.add(observer);


    }

    public void unsubscribe(Observer observer) {
        observers.remove(observer);

    }

    public void updateStock(int newStock) {
        int oldStock = stock;
        stock = newStock;

        if (oldStock == 0 && stock > 0) {
            for (Observer o : observers) {
                o.notify(itemName);
        }

        }
        


    }
}
