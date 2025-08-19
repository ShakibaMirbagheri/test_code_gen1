package com.example;
import java.util.Objects;
public class Person {
    private String uuid;
    private String name;
    private String surname;
    private Integer age;
    public Person(String uuid, String name, String surname, Integer age) {
        this.uuid = uuid;
        this.name = name;
        this.surname = surname;
        this.age = age;
    }
    public String getUuid() {
        return uuid;
    }
    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getSurname() {
        return surname;
    }
    public void setSurname(String surname) {
        this.surname = surname;
    }
    public Integer getAge() {
        return age;
    }
    public void setAge(Integer age) {
        this.age = age;
    }
    @Override
    public String toString() {
        return "Person{" +
                "uuid='" + uuid + '\'' +
                ", name='" + name + '\'' +
                ", surname='" + surname + '\'' +
                ", age=" + age +
                '}';
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return Objects.equals(uuid, person.uuid) &&
                Objects.equals(name, person.name) &&
                Objects.equals(surname, person.surname) &&
                Objects.equals(age, person.age);
    }
    @Override
    public int hashCode() {
        return Objects.hash(uuid, name, surname, age);
    }
}