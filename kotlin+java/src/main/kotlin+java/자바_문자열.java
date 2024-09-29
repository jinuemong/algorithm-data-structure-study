
public class 자바_문자열 {
    public void main(String args []){
        String str = "apple";

        //length
        str.length();
        str.isEmpty();

        str.charAt(0);
        str.indexOf("a");
        str.lastIndexOf("p");

        str.substring(1,3);
        str.substring(3);

        str.replace('p','e');
        str.replaceAll(".","/"); // 모든 문자 치환

        str.replaceFirst("p","e");

        // 자바는 string을 클래스로써 call by reference 형태로 생성 시 주소값 부여
        str.equals("apple");

        // 문자 비교
        str.compareTo("apple");

        str.contains("app");

        str.split(" ");
        str.split("");
        str.trim(); //공백 제거

        Integer.parseInt("100");
        Integer.toString(100);

        // 추가 , 삭제가 가능한 문자열
        StringBuilder sb = new StringBuilder();
        sb.append("apple");

        sb.insert(2,"oo");

        sb.delete(0,2);

        // 특정 인덱스 문자 삭제
        sb.deleteCharAt(2);

        // 특정 인덱스 문자 변경
        sb.setCharAt(1,'p');


        // 문자열 뒤집기
        sb.reverse();

        // 절단
        sb.setLength(2);

        sb.setLength(4); //->공백 채우기
    }
}
